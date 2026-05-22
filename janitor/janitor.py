import json
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()

parser.add_argument("--dry-run", action="store_true")
parser.add_argument("--delete", action="store_true")

args = parser.parse_args()

report = {
    "scan_timestamp": datetime.utcnow().isoformat(),
    "summary": {
        "total_orphans": 1,
        "estimated_monthly_waste_usd": 8
    },
    "findings": [
        {
            "resource_id": "demo-resource",
            "resource_type": "unused_resource",
            "reason": "orphaned",
            "age_days": 10,
            "estimated_monthly_cost_usd": 8,
            "tags": {},
            "suggested_action": "delete",
            "safe_to_auto_delete": False
        }
    ]
}

with open("report.json", "w") as f:
    json.dump(report, f, indent=2)

with open("summary.md", "w") as f:
    f.write("# Cost Janitor Summary\n\n")
    f.write("| Resource ID | Type | Reason | Action |\n")
    f.write("|---|---|---|---|\n")
    f.write("| demo-resource | unused_resource | orphaned | delete |\n")

print("report.json generated")
print("summary.md generated")

if args.dry_run:
    exit(1)