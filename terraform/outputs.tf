# The ECR URL you already have
output "ecr_repository_url" {
  value = aws_ecr_repository.app_repo.repository_url
}

# The public URL for your application
output "app_url" {
  value       = "http://${aws_lb.main.dns_name}"
  description = "The public DNS name of the Load Balancer"
}

# Useful for checking logs in the console
output "cloudwatch_log_group" {
  value = aws_cloudwatch_log_group.app_logs.name
}

# The VPC ID
output "vpc_id" {
  value = aws_vpc.main.id
}