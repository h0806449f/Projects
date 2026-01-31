import boto3
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--profile", required=True)
args = parser.parse_args()

MASTER_ROLE_ARN = "arn:aws:iam::892492072165:role/TerragruntMasterRole"
TARGET_ROLE_NAME = "TerragruntRole"
POLICY_ARN = "arn:aws:iam::aws:policy/AdministratorAccess"

# 建立 boto3 session
session = boto3.Session(profile_name=args.profile)
iam_client = session.client("iam")

trust_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"AWS": "arn:aws:iam::892492072165:root"},
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "AWS:SourceArn": "arn:aws:iam::892492072165:role/TerragruntMasterRole"
                }
            }
        }
    ]
}

# 建立 role
try:
    iam_client.create_role(
        RoleName=TARGET_ROLE_NAME,
        AssumeRolePolicyDocument=json.dumps(trust_policy),
        Description="Role for Terragrunt deployment",
    )
    print(f"Role {TARGET_ROLE_NAME} created")
except iam_client.exceptions.EntityAlreadyExistsException:
    print(f"Role {TARGET_ROLE_NAME} already exists")

# Attach policy
try:
    iam_client.attach_role_policy(
        RoleName=TARGET_ROLE_NAME,
        PolicyArn=POLICY_ARN
    )
    print(f"Attached policy {POLICY_ARN}")
except Exception as e:
    print(f"Failed to attach policy: {e}")
