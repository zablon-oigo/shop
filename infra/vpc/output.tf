output "alb_hostname" {
  value = aws_lb.production.dns_name
}

output "ecs_task_execution_role_arn" {
    value = aws_iam_role.ecs-task-execution-role.arn
    description = "ARN for the ECS Task Execution Role"
}