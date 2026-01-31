data "aws_iam_role" "support_slack_role" {
  name = "AWSSupportSlackAppTFRole-${var.account_id}"
}

resource "awscc_supportapp_slack_channel_configuration" "this" {
  team_id    = var.team_id
  channel_id = var.channel_id
  channel_name = var.channel_name

  notify_on_create_or_reopen_case      = true
  notify_on_add_correspondence_to_case = true
  notify_on_resolve_case               = true
  notify_on_case_severity              = var.notify_on_case_severity

  channel_role_arn = data.aws_iam_role.support_slack_role.arn
}
