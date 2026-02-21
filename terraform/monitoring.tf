# Alarm if CPU stays above 80% for 2 minutes
resource "aws_cloudwatch_metric_alarm" "service_cpu_high" {
  alarm_name          = "ecs-py-app-cpu-high"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = "2"
  metric_name         = "CPUUtilization"
  namespace           = "AWS/ECS"
  period              = "60"
  statistic           = "Average"
  threshold           = "80"

  dimensions = {
    ClusterName = aws_ecs_cluster.main.name
    ServiceName = aws_ecs_service.main.name
  }

  alarm_description = "This alarm monitors high CPU utilization for the ECS service"
}

# Alarm if there are NO healthy tasks (Total Outage)
resource "aws_cloudwatch_metric_alarm" "no_healthy_tasks" {
  alarm_name          = "ecs-py-app-no-healthy-tasks"
  comparison_operator = "LessThanThreshold"
  evaluation_periods  = "1"
  metric_name         = "HealthyHostCount"
  namespace           = "AWS/ApplicationELB"
  period              = "60"
  statistic           = "Minimum"
  threshold           = "1"

  dimensions = {
    TargetGroup  = aws_lb_target_group.app.arn_suffix
    LoadBalancer = aws_lb.main.arn_suffix
  }

  alarm_description = "Triggered if the Load Balancer has 0 healthy tasks."
}