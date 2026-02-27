import json
import sys
import re

# Paths
report_file = sys.argv[1]
tf_file = './terraform/main.tf'

# Load Trivy report
with open(report_file, 'r') as f:
    data = json.load(f)

# Read the Terraform file
with open(tf_file, 'r') as f:
    tf_content = f.read()

# Fixes

# 1️⃣ Fix SSH open to 0.0.0.0/0 → restrict to 10.0.0.0/24
tf_content = re.sub(r'cidr_blocks\s*=\s*\["0.0.0.0/0"\]\s*# ❌ INTENTIONAL VULNERABILITY \(SSH open to world\)',
                    'cidr_blocks = ["10.0.0.0/24"]  # Fixed by AI',
                    tf_content)

# 2️⃣ Enable IMDSv2 on aws_instance
if 'aws_instance "web"' in tf_content:
    if 'metadata_options' not in tf_content:
        tf_content = tf_content.replace(
            'user_data = <<-EOF',
            'metadata_options {\n    http_tokens = "required"\n  }\n\n    user_data = <<-EOF'
        )

# 3️⃣ Encrypt root block device
tf_content = re.sub(r'(aws_instance "web" \{[^}]+)',
                    r'\1\n  root_block_device {\n    encrypted = true\n  }',
                    tf_content, flags=re.DOTALL)

# Save back the fixed Terraform file
with open(tf_file, 'w') as f:
    f.write(tf_content)

print("✅ AI remediation applied: main.tf updated with fixes.") 