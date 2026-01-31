resource "aws_iam_role" "support_slack_role" {
  name = "AWSSupportSlackAppTFRole-${var.account_id}"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Service = "supportapp.amazonaws.com"
      }
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "support_app_full_access" {
  role       = aws_iam_role.support_slack_role.name
  policy_arn = "arn:aws:iam::aws:policy/AWSSupportAppFullAccess"
}

resource "awscc_supportapp_slack_channel_configuration" "this" {
  team_id    = var.team_id
  channel_id = var.channel_id
  channel_name = var.channel_name

  notify_on_create_or_reopen_case      = true
  notify_on_add_correspondence_to_case = true
  notify_on_resolve_case               = true
  notify_on_case_severity              = var.notify_on_case_severity

  channel_role_arn = aws_iam_role.support_slack_role.arn
}
