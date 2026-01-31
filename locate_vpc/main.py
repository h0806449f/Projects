import os
import csv
import asyncio
import subprocess
import pandas as pd
from datetime import datetime


# list updated on 2025-11-13
account_list = [
    "ai_genai_prod",
    "ai_genaipoc_dev",
    "app_alpha",
    "app_au",
    "app_mo",
    "app_ops",
    "app_pu",
    "app_sandbox",
    "app_sharedservice",
    "app_stage",
    "app_star",
    "app_um",
    "app_vjp",
    "app_vt",
    "audit",
    "bit_bybit",
    "bit_cashier",
    "bit_finance",
    "bit_pub",
    "bit_service",
    "bit_shared_service",
    "bit_uat",
    "bit_vts",
    "cis",
    "cis_noc",
    "create_gold_technology_limited",
    "crm_alpha01",
    "crm_at",
    "crm_au",
    "crm_mo",
    "crm_ops",
    "crm_pu",
    "crm_pub",
    "crm_sandbox",
    "crm_star",
    "crm_um",
    "crm_vjp",
    "crm_vt",
    "finance_datalake",
    "gbis",
    "gbis_datawind",
    "ha_cps",
    "ha_cps_dev",
    "ha_cps_sandbox",
    "hr",
    "log_archive",
    "mts_business",
    "network_account",
    "network_staging",
    "payment_datalake",
    "risk_antifraud_prod",
    "risk_antifraud_test",
    "risk_datalake",
    "risk_datalake_dev",
    "risk_hs",
    "risk_infra",
    "risk_infra_dev",
    "risk_insight",
    "risk_pe",
    "risk_pe_dev",
    "risk_rc",
    "risk_rnd",
    "risk_saas",
    "risk_taipei_data",
    "risk_wt",
    "shared_service_account",
    "star_bi",
    "unicorn",
    "vantage_international_group_limited",
    "webteam_officialsite",
    "data_governance",
]

# 併發上限
MAX_CONCURRENT = 10
semaphore = asyncio.Semaphore(MAX_CONCURRENT)

# 第一階段, 找出各個 account 哪些有 VPC 
async def assume_role_and_find_vpc_region(account):
    async with semaphore:
        command = f"aws-vault exec {account} -- python3 01_locate_regions_with_vpc.py {account}"
        print(f"🔄 Start: {account}")

        process = await asyncio.create_subprocess_shell(
            command,
            executable="/bin/bash",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await process.communicate()

        if process.returncode == 0:
            print(f"✅ Done: {account}")
        else:
            print(f"❌ Failed: {account}")
            print(stderr.decode())

async def run_aggregation():
    print("🔄 Aggregating data...")
    process = await asyncio.create_subprocess_shell(
        "python3 02_sort_regions_of_vpc.py",
        executable="/bin/bash",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    if process.returncode == 0:
        print("✅ Aggregation complete.")
    else:
        print("❌ Aggregation failed.")
        print(stderr.decode())

def cleanup_files():
    files_to_delete = [
        "RAWDATA_vpc_details.csv",
        "RAWDATA_vpc_details.csv.lock",
        "RAWDATA_vpc_summary.csv",
        "RAWDATA_vpc_summary.csv.lock"
    ]
    print("🧹 Starting file cleanup...")
    for file in files_to_delete:
        try:
            if os.path.exists(file):
                os.remove(file)
                print(f"🗑️ Deleted: {file}")
            else:
                print(f"ℹ️ File not found, skipping: {file}")
        except Exception as e:
            print(f"❌ Error deleting {file}: {str(e)}")
    print("✅ Cleanup complete.")


# 第二階段, 整理 VPC 相關資訊
async def assume_role_and_query_vpc_info(account: str, region: str):
    async with semaphore:
        command = f"aws-vault exec {account} --region {region} -- python3 03_query_vpc_info.py {region}"
        print(f"🔄 Start: account={account} region={region}")

        process = await asyncio.create_subprocess_shell(
            command,
            executable="/bin/bash",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        stdout, stderr = await process.communicate()

        if process.returncode == 0:
            print(f"✅ Done: account={account} region={region}")
        else:
            print(f"❌ Failed: account={account} region={region}")
            print(stderr.decode())

async def sort_csv():
    print("🔄 Starting sorting CSV...")
    process = await asyncio.create_subprocess_shell(
        "python3 04_sort_csv.py",
        executable="/bin/bash",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    if process.returncode == 0:
        print("✅ Sorting complete.")
    else:
        print("❌ Sorting failed.")
        print(stderr.decode())

# 第三階段, 併發完畢後, 整理最終 csv
def final_sort():
    # 今天日期 (YYYYMMDD)
    today = datetime.today().strftime("%Y%m%d")
    output_file = f"result_{today}.csv"

    # CSV: read, filter columns
    df = pd.read_csv("vpc_networking_info.csv")
    df = df[["AccountName", "Account", "Region", "VpcName", "VpcId", "VpcCidr"]]

    # CSV: remove _read in AccountName
    df["AccountName"] = df["AccountName"].str.replace("_read", "", regex=False)

    # CSV: unique, sort, output
    df_unique = df.drop_duplicates()
    df_unique = df_unique.sort_values(by=["AccountName", "Account", "Region", "VpcName"])
    df_unique.to_csv(output_file, index=False)

    return output_file

def final_cleanup():
    file_list = ["vpc_networking_sorted.csv", "vpc_networking.csv", "vpc_transit_gateway_sorted.csv", "vpc_transit_gateway.csv"]
    for f in file_list:
        if os.path.exists(f):
            os.remove(f)
            print(f"已刪除檔案: {f}")
        else:
            print(f"檔案不存在: {f}")

async def main():
    # 第一階段
    tasks = [assume_role_and_find_vpc_region(account) for account in account_list]
    await asyncio.gather(*tasks)
    await run_aggregation()
    cleanup_files()

    # 第二階段
    account_region_pairs = []

    with open('00_account_region_mapping.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            account = row['Account'].strip()
            regions = [r.strip() for r in row['Activate_Region'].split(',')]
            for region in regions:
                account_region_pairs.append((account, region))

    tasks = [assume_role_and_query_vpc_info(account, region) for account, region in account_region_pairs]
    await asyncio.gather(*tasks)
    await sort_csv()

    # 第三階段
    final_sort()
    final_cleanup()




if __name__ == "__main__":
    asyncio.run(main())