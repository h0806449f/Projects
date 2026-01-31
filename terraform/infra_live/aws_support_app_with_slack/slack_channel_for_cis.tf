module "support_app_ai_genai_prod" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.ai_genai_prod
  providers = {
    aws   = aws.ai_genai_prod
    awscc = awscc.ai_genai_prod
  }
}

module "support_app_ai_genaipoc_dev" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.ai_genaipoc_dev
  providers = {
    aws   = aws.ai_genaipoc_dev
    awscc = awscc.ai_genaipoc_dev
  }
}

module "support_app_app_alpha" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.app_alpha
  providers = {
    aws   = aws.app_alpha
    awscc = awscc.app_alpha
  }
}

module "support_app_app_au" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.app_au
  providers = {
    aws   = aws.app_au
    awscc = awscc.app_au
  }
}

module "support_app_app_mo" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.app_mo
  providers = {
    aws   = aws.app_mo
    awscc = awscc.app_mo
  }
}

module "support_app_app_ops" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.app_ops
  providers = {
    aws   = aws.app_ops
    awscc = awscc.app_ops
  }
}

module "support_app_app_pu" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.app_pu
  providers = {
    aws   = aws.app_pu
    awscc = awscc.app_pu
  }
}

module "support_app_app_sandbox" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.app_sandbox
  providers = {
    aws   = aws.app_sandbox
    awscc = awscc.app_sandbox
  }
}

module "support_app_app_sharedservice" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.app_sharedservice
  providers = {
    aws   = aws.app_sharedservice
    awscc = awscc.app_sharedservice
  }
}

module "support_app_app_stage" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.app_stage
  providers = {
    aws   = aws.app_stage
    awscc = awscc.app_stage
  }
}

module "support_app_app_star" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.app_star
  providers = {
    aws   = aws.app_star
    awscc = awscc.app_star
  }
}

module "support_app_app_um" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.app_um
  providers = {
    aws   = aws.app_um
    awscc = awscc.app_um
  }
}

module "support_app_app_vjp" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.app_vjp
  providers = {
    aws   = aws.app_vjp
    awscc = awscc.app_vjp
  }
}

module "support_app_app_vt" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.app_vt
  providers = {
    aws   = aws.app_vt
    awscc = awscc.app_vt
  }
}

module "support_app_audit" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.audit
  providers = {
    aws   = aws.audit
    awscc = awscc.audit
  }
}

module "support_app_bit_bybit" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.bit_bybit
  providers = {
    aws   = aws.bit_bybit
    awscc = awscc.bit_bybit
  }
}

module "support_app_bit_cashier" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.bit_cashier
  providers = {
    aws   = aws.bit_cashier
    awscc = awscc.bit_cashier
  }
}

module "support_app_bit_finance" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.bit_finance
  providers = {
    aws   = aws.bit_finance
    awscc = awscc.bit_finance
  }
}

module "support_app_bit_pub" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.bit_pub
  providers = {
    aws   = aws.bit_pub
    awscc = awscc.bit_pub
  }
}

module "support_app_bit_service" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.bit_service
  providers = {
    aws   = aws.bit_service
    awscc = awscc.bit_service
  }
}

module "support_app_bit_shared_service" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.bit_shared_service
  providers = {
    aws   = aws.bit_shared_service
    awscc = awscc.bit_shared_service
  }
}

module "support_app_bit_uat" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.bit_uat
  providers = {
    aws   = aws.bit_uat
    awscc = awscc.bit_uat
  }
}

module "support_app_bit_vts" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.bit_vts
  providers = {
    aws   = aws.bit_vts
    awscc = awscc.bit_vts
  }
}

module "support_app_cis" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.cis
  providers = {
    aws   = aws.cis
    awscc = awscc.cis
  }
}

module "support_app_cis_noc" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.cis_noc
  providers = {
    aws   = aws.cis_noc
    awscc = awscc.cis_noc
  }
}

module "support_app_create_gold_technology_limited" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.create_gold_technology_limited
  providers = {
    aws   = aws.create_gold_technology_limited
    awscc = awscc.create_gold_technology_limited
  }
}

module "support_app_crm_alpha01" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.crm_alpha01
  providers = {
    aws   = aws.crm_alpha01
    awscc = awscc.crm_alpha01
  }
}

module "support_app_crm_at" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.crm_at
  providers = {
    aws   = aws.crm_at
    awscc = awscc.crm_at
  }
}

module "support_app_crm_au" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.crm_au
  providers = {
    aws   = aws.crm_au
    awscc = awscc.crm_au
  }
}

module "support_app_crm_mo" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.crm_mo
  providers = {
    aws   = aws.crm_mo
    awscc = awscc.crm_mo
  }
}

module "support_app_crm_ops" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.crm_ops
  providers = {
    aws   = aws.crm_ops
    awscc = awscc.crm_ops
  }
}

module "support_app_crm_pu" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.crm_pu
  providers = {
    aws   = aws.crm_pu
    awscc = awscc.crm_pu
  }
}

module "support_app_crm_pub" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.crm_pub
  providers = {
    aws   = aws.crm_pub
    awscc = awscc.crm_pub
  }
}

module "support_app_crm_sandbox" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.crm_sandbox
  providers = {
    aws   = aws.crm_sandbox
    awscc = awscc.crm_sandbox
  }
}

module "support_app_crm_star" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.crm_star
  providers = {
    aws   = aws.crm_star
    awscc = awscc.crm_star
  }
}

module "support_app_crm_um" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.crm_um
  providers = {
    aws   = aws.crm_um
    awscc = awscc.crm_um
  }
}

module "support_app_crm_vjp" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.crm_vjp
  providers = {
    aws   = aws.crm_vjp
    awscc = awscc.crm_vjp
  }
}

module "support_app_crm_vt" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.crm_vt
  providers = {
    aws   = aws.crm_vt
    awscc = awscc.crm_vt
  }
}

module "support_app_finance_datalake" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.finance_datalake
  providers = {
    aws   = aws.finance_datalake
    awscc = awscc.finance_datalake
  }
}

module "support_app_gbis" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.gbis
  providers = {
    aws   = aws.gbis
    awscc = awscc.gbis
  }
}

module "support_app_gbis_datawind" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.gbis_datawind
  providers = {
    aws   = aws.gbis_datawind
    awscc = awscc.gbis_datawind
  }
}

module "support_app_ha_cps" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.ha_cps
  providers = {
    aws   = aws.ha_cps
    awscc = awscc.ha_cps
  }
}

module "support_app_ha_cps_dev" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.ha_cps_dev
  providers = {
    aws   = aws.ha_cps_dev
    awscc = awscc.ha_cps_dev
  }
}

module "support_app_ha_cps_sandbox" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.ha_cps_sandbox
  providers = {
    aws   = aws.ha_cps_sandbox
    awscc = awscc.ha_cps_sandbox
  }
}

module "support_app_hr" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.hr
  providers = {
    aws   = aws.hr
    awscc = awscc.hr
  }
}

module "support_app_log_archive" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.log_archive
  providers = {
    aws   = aws.log_archive
    awscc = awscc.log_archive
  }
}

module "support_app_mts_business" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.mts_business
  providers = {
    aws   = aws.mts_business
    awscc = awscc.mts_business
  }
}

module "support_app_network_account" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.network_account
  providers = {
    aws   = aws.network_account
    awscc = awscc.network_account
  }
}

module "support_app_network_staging" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.network_staging
  providers = {
    aws   = aws.network_staging
    awscc = awscc.network_staging
  }
}

module "support_app_payment_datalake" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.payment_datalake
  providers = {
    aws   = aws.payment_datalake
    awscc = awscc.payment_datalake
  }
}

module "support_app_risk_antifraud_prod" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.risk_antifraud_prod
  providers = {
    aws   = aws.risk_antifraud_prod
    awscc = awscc.risk_antifraud_prod
  }
}

module "support_app_risk_antifraud_test" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.risk_antifraud_test
  providers = {
    aws   = aws.risk_antifraud_test
    awscc = awscc.risk_antifraud_test
  }
}

module "support_app_risk_datalake" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.risk_datalake
  providers = {
    aws   = aws.risk_datalake
    awscc = awscc.risk_datalake
  }
}

module "support_app_risk_datalake_dev" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.risk_datalake_dev
  providers = {
    aws   = aws.risk_datalake_dev
    awscc = awscc.risk_datalake_dev
  }
}

module "support_app_risk_hs" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.risk_hs
  providers = {
    aws   = aws.risk_hs
    awscc = awscc.risk_hs
  }
}

module "support_app_risk_infra" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.risk_infra
  providers = {
    aws   = aws.risk_infra
    awscc = awscc.risk_infra
  }
}

module "support_app_risk_infra_dev" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.risk_infra_dev
  providers = {
    aws   = aws.risk_infra_dev
    awscc = awscc.risk_infra_dev
  }
}

module "support_app_risk_insight" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.risk_insight
  providers = {
    aws   = aws.risk_insight
    awscc = awscc.risk_insight
  }
}

module "support_app_risk_pe" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.risk_pe
  providers = {
    aws   = aws.risk_pe
    awscc = awscc.risk_pe
  }
}

module "support_app_risk_pe_dev" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.risk_pe_dev
  providers = {
    aws   = aws.risk_pe_dev
    awscc = awscc.risk_pe_dev
  }
}

module "support_app_risk_rc" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.risk_rc
  providers = {
    aws   = aws.risk_rc
    awscc = awscc.risk_rc
  }
}

module "support_app_risk_rnd" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.risk_rnd
  providers = {
    aws   = aws.risk_rnd
    awscc = awscc.risk_rnd
  }
}

module "support_app_risk_saas" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.risk_saas
  providers = {
    aws   = aws.risk_saas
    awscc = awscc.risk_saas
  }
}

module "support_app_risk_taipei_data" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.risk_taipei_data
  providers = {
    aws   = aws.risk_taipei_data
    awscc = awscc.risk_taipei_data
  }
}

module "support_app_risk_wt" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.risk_wt
  providers = {
    aws   = aws.risk_wt
    awscc = awscc.risk_wt
  }
}

module "support_app_shared_service_account" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.shared_service_account
  providers = {
    aws   = aws.shared_service_account
    awscc = awscc.shared_service_account
  }
}

module "support_app_star_bi" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.star_bi
  providers = {
    aws   = aws.star_bi
    awscc = awscc.star_bi
  }
}

module "support_app_unicorn" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.unicorn
  providers = {
    aws   = aws.unicorn
    awscc = awscc.unicorn
  }
}

module "support_app_vantage_international_group_limited" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.vantage_international_group_limited
  providers = {
    aws   = aws.vantage_international_group_limited
    awscc = awscc.vantage_international_group_limited
  }
}

module "support_app_webteam_officialsite" {
  source   = "../../modules/aws_support_app_with_slack"
  team_id      = "T08F51GBMC4"
  channel_id   = "C0A3RNHRV7Y"
  channel_name = "ext-hytech-cis-aws"
  notify_on_case_severity = "high"

  account_id = local.accounts.webteam_officialsite
  providers = {
    aws   = aws.webteam_officialsite
    awscc = awscc.webteam_officialsite
  }
}

