import json
import sys

# Read Trivy JSON report
report_file = sys.argv[1]
with open(report_file, 'r') as f:
    data = json.load(f)

print("\n=== AI-Based Remediation Suggestions ===\n")

for result in data.get('Results', []):
    for misconf in result.get('Misconfigurations', []):
        severity = misconf.get('Severity', 'UNKNOWN')
        title = misconf.get('Title', 'No Title')
        description = misconf.get('Description', '')

        if severity in ['HIGH', 'CRITICAL']:
            print(f"- {title} [{severity}]")
            print(f"  Suggestion: {description}\n")

print("=== End of AI Suggestions ===\n")