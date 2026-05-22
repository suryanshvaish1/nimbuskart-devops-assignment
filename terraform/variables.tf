variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "environment" {
  type    = string
  default = "staging"
}

variable "project" {
  type    = string
  default = "NimbusKart"
}

variable "owner" {
  type    = string
  default = "Suryansh"
}

variable "ssh_cidr" {
  type    = string
  default = "0.0.0.0/0"
}