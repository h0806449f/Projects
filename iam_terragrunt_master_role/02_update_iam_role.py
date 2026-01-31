import boto3
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--profile", required=True)
args = parser.parse_args()

MASTER_ROLE_ARN = "arn:aws:iam::892492072165:role/TerragruntMasterRole"
TARGET_ROLE_NAME = "TerragruntRole"
POLICY_ARN = "arn:aws:iam::aws:policy/AdministratorAccess"

session = boto3.Session(profile_name=args.profile)
iam_client = session.client("iam")

trust_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": MASTER_ROLE_ARN
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

# 1️⃣ 建立 role（若不存在）
try:
    iam_client.create_role(
        RoleName=TARGET_ROLE_NAME,
        AssumeRolePolicyDocument=json.dumps(trust_policy),
        Description="Role for Terragrunt deployment",
    )
    print(f"✅ Role {TARGET_ROLE_NAME} created")
except iam_client.exceptions.EntityAlreadyExistsException:
    print(f"ℹ️ Role {TARGET_ROLE_NAME} already exists")

    # 2️⃣ **重點：更新 trust policy**
    iam_client.update_assume_role_policy(
        RoleName=TARGET_ROLE_NAME,
        PolicyDocument=json.dumps(trust_policy),
    )
    print(f"🔄 Trust policy updated for {TARGET_ROLE_NAME}")

# 3️⃣ Attach permission policy（可重跑）
iam_client.attach_role_policy(
    RoleName=TARGET_ROLE_NAME,
    PolicyArn=POLICY_ARN
)
print(f"✅ Attached policy {POLICY_ARN}")
