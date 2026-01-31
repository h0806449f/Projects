terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5"
    }
    awscc = {
      source  = "hashicorp/awscc"
      version = ">= 0.6"
    }
  }
}
