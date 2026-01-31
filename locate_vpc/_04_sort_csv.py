import pandas as pd
import os
import json
import logging

logging.basicConfig(
    filename='vpc_postprocess.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

def sort_csv_file(input_csv_path, sort_columns, output_csv_path):
    if not os.path.exists(input_csv_path):
        logging.warning(f"File {input_csv_path} not found.")
        return

    try:
        df = pd.read_csv(input_csv_path, dtype=str)
        df_sorted = df.sort_values(by=sort_columns)
        df_sorted.to_csv(output_csv_path, index=False)
        logging.info(f"Sorted file saved to {output_csv_path}")
    except Exception as e:
        logging.error(f"Failed to sort {input_csv_path}: {e}")

def add_account_name(mapping_file, csv_file, output_file):
    if not os.path.exists(mapping_file):
        logging.error(f"Mapping file {mapping_file} not found.")
        return
    if not os.path.exists(csv_file):
        logging.error(f"CSV file {csv_file} not found.")
        return

    try:
        with open(mapping_file, "r") as f:
            mapping_data = json.load(f)

        mapping_df = pd.DataFrame(mapping_data)
        mapping_df = mapping_df.rename(columns={"AccountId": "Account"})

        data_df = pd.read_csv(csv_file, dtype=str)
        merged_df = data_df.merge(mapping_df, on="Account", how="left")

        if "AccountName" not in merged_df.columns:
            logging.warning(f"AccountName column not added for {csv_file}. Check mapping file.")
        else:
            logging.info(f"Added AccountName to {csv_file}.")

        # 重新排序欄位：Account, AccountName 放在最前面
        columns = merged_df.columns.tolist()
        new_order = ['AccountName', 'Account'] + [col for col in columns if col not in ['Account', 'AccountName']]
        merged_df = merged_df[new_order]

        merged_df.to_csv(output_file, index=False)
        logging.info(f"Output file saved to {output_file}")
    except Exception as e:
        logging.error(f"Failed to enrich {csv_file} with account names: {e}")


def main():
    # Sort and enrich VPC networking CSV
    sort_csv_file(
        input_csv_path="vpc_networking.csv",
        sort_columns=['Account', 'Region', 'VpcName', 'VpcCidr', 'SubnetCidr'],
        output_csv_path="vpc_networking_sorted.csv"
    )
    add_account_name(
        mapping_file="account_mapping.json",
        csv_file="vpc_networking_sorted.csv",
        output_file="vpc_networking_info.csv"
    )

    # Sort and enrich Transit Gateway CSV
    sort_csv_file(
        input_csv_path="vpc_transit_gateway.csv",
        sort_columns=['Account', 'TransitGatewayAttachmentType', 'TransitGatewayId'],
        output_csv_path="vpc_transit_gateway_sorted.csv"
    )
    add_account_name(
        mapping_file="account_mapping.json",
        csv_file="vpc_transit_gateway_sorted.csv",
        output_file="vpc_transit_gateway_info.csv"
    )

if __name__ == "__main__":
    main()
