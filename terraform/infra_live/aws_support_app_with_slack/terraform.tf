terraform {
  required_version = ">= 1.3"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5"
    }
  }

  backend "s3" {
    bucket = "nv-unicorn-terraform-prod-s3bucket-state-file"
    key = "aws_support_app_with_slack/terraform.tfstate"
    region = "us-east-1"
    profile = "unicorn"
    encrypt = true
  }
}