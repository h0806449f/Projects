import boto3
import sys
import pandas as pd
from filelock import FileLock
import os
import logging

# 設置日誌
logging.basicConfig(
    filename='vpc_check.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

def find_vpcs_by_tag(account_name: str, tag_key='Name'):
    try:
        ec2_client = boto3.client('ec2')
        regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
        
        vpcs_with_tags = []
        
        for region in regions:
            logging.info(f"[{account_name}] Checking region: {region}")
            print(f"[{account_name}] Checking region: {region}")
            try:
                ec2 = boto3.client('ec2', region_name=region)
                vpcs = ec2.describe_vpcs().get('Vpcs', [])
                
                for vpc in vpcs:
                    tags = vpc.get('Tags', [])
                    for tag in tags:
                        if tag['Key'] == tag_key:
                            vpcs_with_tags.append({
                                'Account': account_name,
                                'Region': region,
                                'VpcId': vpc['VpcId']
                            })
                            break
            except Exception as e:
                logging.error(f"[{account_name}] Error in region {region}: {e}")
                print(f"[{account_name}] Error in region {region}: {e}")
                continue
        
        return vpcs_with_tags, regions
    
    except Exception as e:
        logging.error(f"[{account_name}] Failed to initialize EC2 client: {e}")
        print(f"[{account_name}] Failed to initialize EC2 client: {e}")
        return [], []

def process_vpc_df(df: pd.DataFrame, account_name: str):
    # 取得唯一 Account & Region
    unique_account_region = df[['Account', 'Region']].drop_duplicates()
    
    # lock 寫入單一 CSV，使用檔案鎖定，避免寫入錯誤
    summary_csv = 'RAWDATA_vpc_summary.csv'
    lock_file = f"{summary_csv}.lock"
    
    with FileLock(lock_file):
        header = not os.path.exists(summary_csv)
        unique_account_region.to_csv(summary_csv, mode='a', index=False, header=header)
    
    # 可選：寫入詳細資料到 vpc_details.csv
    details_csv = 'RAWDATA_vpc_details.csv'
    lock_details = f"{details_csv}.lock"
    
    with FileLock(lock_details):
        header = not os.path.exists(details_csv)
        df.to_csv(details_csv, mode='a', index=False, header=header)
    
    logging.info(f"✅ [{account_name}] Exported data to: {summary_csv} and {details_csv}")
    print(f"✅ [{account_name}] Exported data to: {summary_csv} and {details_csv}")

if __name__ == "__main__":
    # 1. after assume role
    if len(sys.argv) != 2:
        logging.error("Usage: python locate_vpc_region.py <account_name>")
        print("Usage: python locate_vpc_region.py <account_name>")
        sys.exit(1)

    account_name = sys.argv[1]

    # 2. check each region contains VPC ?
    vpc_data, region_list = find_vpcs_by_tag(account_name)

    if vpc_data:
        # 3. write data
        df = pd.DataFrame(vpc_data)
        process_vpc_df(df, account_name)
    else:
        logging.warning(f"⚠️ No VPCs with tag 'Name' found in account: {account_name}")
        print(f"⚠️ No VPCs with tag 'Name' found in account: {account_name}")