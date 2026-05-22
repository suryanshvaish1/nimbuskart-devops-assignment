
---

# SUBMISSION.md

```md id="x2"
# Submission — DevOps Engineer Assignment

**Candidate name:** Suryansh Vaish  
**Email:** your-email@example.com  
**Date submitted:** 2026-05-22  
**Hours spent (approximate):** 8

## Deliverables checklist

- [x] Part A: Terraform code under /terraform applies cleanly on LocalStack
- [x] Part A: `terraform validate` and `terraform fmt -check` both pass
- [x] Part B: Janitor script runs in --dry-run mode and produces report.json
- [x] Part B: GitHub Actions workflow runs green on a fresh PR
- [x] Part B: --delete mode respects Protected=true tag
- [x] Part C: DESIGN.md is present and within 2 pages
- [x] Walkthrough video link below is accessible (unlisted is fine)

## Walkthrough video

Link (Loom / YouTube unlisted / Google Drive):
https://drive.google.com/file/d/15XEb8NgSmNMgCCcQUEK9lbf8Mi5A2cWZ/view?usp=drivesdk

Length: max 5 minutes

## Sample report

Path to a sample report.json produced by your script:

samples/report.example.json

## Known limitations

- LocalStack does not fully emulate all AWS APIs.
- Static pricing is approximate.
- No real AWS account integration.
- Simplified cleanup workflow for demo purposes.

## AI usage disclosure

ChatGPT and GitHub Copilot were used for debugging, Terraform structure guidance, and CI workflow assistance.
