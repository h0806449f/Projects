import asyncio
import subprocess
from datetime import datetime

# 69 個 AWS profile name
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
    "vantage_international_group_limited",
    "webteam_officialsite"
]

MAX_CONCURRENT = 10
semaphore = asyncio.Semaphore(MAX_CONCURRENT)

async def create_iam_role_in_account(account):
    async with semaphore:
        command = f"aws-vault exec {account} -- python3 01_create_iam_role.py --profile {account}"
        print(f"🔄 Start deploying IAM role: {account}")

        process = await asyncio.create_subprocess_shell(
            command,
            executable="/bin/bash",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await process.communicate()

        if process.returncode == 0:
            print(f"✅ IAM role deployed: {account}")
        else:
            print(f"❌ Failed deploying IAM role: {account}")
            print(stderr.decode())

async def main():
    tasks = [create_iam_role_in_account(account) for account in account_list]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
