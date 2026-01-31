import boto3
import pandas as pd
from pprint import pprint
import os
import logging
from filelock import FileLock

logging.basicConfig(
    filename='vpc_check.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

def get_tag_value(tags, key):
    return next((tag['Value'] for tag in tags if tag['Key'] == key), '')

def get_current_region():
    try:
        ec2 = boto3.client('ec2')
        region = ec2.meta.region_name
        if region:
            return region
    except Exception:
        pass
    return os.environ.get("AWS_REGION") or os.environ.get("AWS_DEFAULT_REGION")

def safe_write_csv(df: pd.DataFrame, filename: str):
    lock_path = filename + ".lock"
    with FileLock(lock_path):
        header = not os.path.exists(filename)
        df.to_csv(filename, mode='a', index=False, header=header)
    logging.info(f"Write to {filename} completed with lock.")

def collect_vpc_and_tgw_info():
    ec2 = boto3.client('ec2')
    sts = boto3.client('sts')
    account_id = sts.get_caller_identity()['Account']
    region = get_current_region()

    vpc_networking_records = []
    tgw_attachment_records = []

    # 取得所有 VPC
    vpcs = ec2.describe_vpcs().get('Vpcs', [])

    # 建立 VPC Name Map & CIDR Map（包含 secondary CIDR）
    vpc_map = {}
    vpc_cidr_map = {}
    for v in vpcs:
        if v.get('IsDefault', False):
            continue
        vpc_id = v['VpcId']
        vpc_name = get_tag_value(v.get('Tags', []), 'Name')
        vpc_map[vpc_id] = vpc_name

        # 收集所有 CIDR block（primary + secondary）
        cidrs = [assoc['CidrBlock'] for assoc in v.get('CidrBlockAssociationSet', [])]
        vpc_cidr_map[vpc_id] = ', '.join(cidrs)  # 用逗號分隔

    # 取得所有 Subnet
    subnets = ec2.describe_subnets().get('Subnets', [])
    for subnet in subnets:
        vpc_id = subnet['VpcId']
        if vpc_id not in vpc_map:
            continue
        subnet_id = subnet['SubnetId']
        subnet_cidr = subnet.get('CidrBlock', '')
        subnet_name = get_tag_value(subnet.get('Tags', []), 'Name')

        vpc_networking_records.append({
            'Account': account_id,
            'Region': region,
            'VpcName': vpc_map.get(vpc_id, ''),
            'VpcId': vpc_id,
            'VpcCidr': vpc_cidr_map.get(vpc_id, ''),
            'SubnetName': subnet_name,
            'SubnetId': subnet_id,
            'SubnetCidr': subnet_cidr
        })

    # 取得 TGW 與 attachments
    tgw_list = ec2.describe_transit_gateways().get('TransitGateways', [])
    tgw_id_name_map = {
        tgw['TransitGatewayId']: get_tag_value(tgw.get('Tags', []), 'Name')
        for tgw in tgw_list
    }

    attachments = ec2.describe_transit_gateway_attachments().get('TransitGatewayAttachments', [])
    for att in attachments:
        attachment_id = att['TransitGatewayAttachmentId']
        tgw_id = att['TransitGatewayId']
        tgw_name = tgw_id_name_map.get(tgw_id, '')
        resource_type = att.get('ResourceType', '')
        resource_id = att.get('ResourceId', '')
        owner_id = att.get('TransitGatewayOwnerId', '') # 20260107 test added

        tgw_attachment_records.append({
            'Account': account_id,
            'Region': region,
            'TransitGatewayName': tgw_name,
            'TransitGatewayId': tgw_id,
            'TransitGatewayAttachmentType': resource_type,
            'TransitGatewayAttachmentId': attachment_id,
            'ResourceId': resource_id,
            'TransitGatewayOwnerId': owner_id,          # 20260107 test added
        })

    return vpc_networking_records, tgw_attachment_records


def main():
    VPC_CSV = "vpc_networking.csv"
    TGW_CSV = "vpc_transit_gateway.csv"

    vpc_net_records, tgw_records = collect_vpc_and_tgw_info()

    if vpc_net_records:
        vpc_net_df = pd.DataFrame(vpc_net_records)
        safe_write_csv(vpc_net_df, VPC_CSV)
    else:
        logging.info("No VPC records to write.")

    if tgw_records:
        tgw_df = pd.DataFrame(tgw_records)
        safe_write_csv(tgw_df, TGW_CSV)
    else:
        logging.info("No Transit Gateway records to write.")

    if vpc_net_records:
        print("\n=== VPC Networking ===")
        pprint(vpc_net_df.to_dict(orient='records'))

    if tgw_records:
        print("\n=== Transit Gateway Attachments ===")
        pprint(tgw_df.to_dict(orient='records'))

if __name__ == "__main__":
    main()
