# NimbusKart DevOps Assignment

## Overview

This project implements a multi-cloud cost hygiene and automation solution for NimbusKart using Terraform, LocalStack, Python, and GitHub Actions.

The project provisions AWS infrastructure locally using LocalStack and implements a Cost Janitor automation tool that detects orphaned and wasteful cloud resources.

---

## How to run locally

### Clone Repository


git clone <repo-url>
cd nimbuskart-devops-assignment
Start LocalStack
docker run --rm -d -p 4566:4566 --name localstack localstack/localstack
Apply Terraform
cd terraform

terraform init
terraform fmt
terraform validate
terraform apply -auto-approve

Run Cost Janitor
cd ../janitor

pip install -r requirements.txt

python janitor.py --dry-run
Run Delete Mode
python janitor.py --delete
Architecture
Developer
   |
   v
Terraform --> LocalStack --> Mock AWS Resources
   |
   v
GitHub Actions --> Cost Janitor --> report.json + summary.md
Decisions & deviations
SSH access from 0.0.0.0/0 is insecure and should be restricted in production.
Auto-delete is disabled by default to avoid accidental outages.
LocalStack behavior may differ slightly from real AWS services.
Static pricing estimates are approximate and not real-time AWS pricing.
Protected=true tag prevents destructive operations for safety.
Trade-offs

With one more week, I would:

Add multi-cloud support for GCP and Azure.
Add CloudWatch metrics and dashboards.
Add automated Slack notifications.
Add Terraform remote state support.
Add full unit and integration test coverage.

AI usage disclosure

Tools used:

ChatGPT for Terraform debugging and workflow guidance.
GitHub Copilot for boilerplate generation.

One incorrect AI suggestion:

AI initially suggested insecure delete logic without safety validation. I corrected this by adding Protected=true checks.

Code written manually:

The orphan detection logic and tagging validation were manually implemented to ensure full understanding of the workflow.