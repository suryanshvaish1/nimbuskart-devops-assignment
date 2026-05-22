locals {
  common_tags = {
    Project     = var.project
    Environment = var.environment
    Owner       = var.owner
    ManagedBy   = "terraform"
  }
}

resource "null_resource" "demo_resource" {
  triggers = {
    project = var.project
  }
}