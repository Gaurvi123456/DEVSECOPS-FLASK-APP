import json
import sys

report_file = sys.argv[1]

with open(report_file, 'r') as f:
    data = json.load(f)

high_critical = []

for result in data.get('Results', []):
    for misconf in result.get('Misconfigurations', []):
        severity = misconf.get('Severity', '')
        title = misconf.get('Title', '')
        if severity in ['HIGH', 'CRITICAL']:
            high_critical.append(f"{title} [{severity}]")

if high_critical:
    print("❌ High/Critical issues detected:")
    for item in high_critical:
        print(" -", item)
    sys.exit(1)
else:
    print("✅ No HIGH/CRITICAL issues found. Pipeline can pass.")