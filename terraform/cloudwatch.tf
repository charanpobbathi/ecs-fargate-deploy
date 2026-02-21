resource "aws_cloudwatch_log_group" "app_logs" {
  name              = "/ecs/ecr-fargate-py-app"
  retention_in_days = 7
}