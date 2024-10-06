resource "aws_alb_target_group" "default-target-group"{
    name     = "${var.ecs_cluster_name}-tg"
    port     = 80
    protocol = "HTTP"
    health_check {
    path                = var.health_check_path
    port                = "traffic-port"
    healthy_threshold   = 5
    unhealthy_threshold = 2
    timeout             = 2
    interval            = 5
    matcher             = "200"
  }

}
resource "aws_alb_listener" "ecs-alb-http-listener" {
  load_balancer_arn = aws_lb.production.id
  port              = "80"
  protocol          = "HTTP"
  depends_on        = [aws_alb_target_group.default-target-group]
    default_action {
    type             = "forward"
    target_group_arn = aws_alb_target_group.default-target-group.arn
  }
}