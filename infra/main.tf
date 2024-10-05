provider "aws" {
    region = "${var.region}"
    access_key = "${var.access_key}"
    secret_key = "${var.secret_key}"
    token = "${var.token}"
}
module "vpc" {
    source = "./vpc"
}
module "ecs" {
    source = "./ecs"
}