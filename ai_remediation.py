import json

# Read Trivy JSON report
with open("trivy-report.json", "r") as f:
    data = json.load(f)

# Open the Terraform file
tf_file = "terraform/main.tf"
with open(tf_file, "r") as f:
    tf_lines = f.readlines()

# Fixes mapping
new_tf_lines = []
inside_sg_block = False

for line in tf_lines:
    stripped = line.strip()

    # Detect start of aws_security_group block
    if stripped.startswith('resource "aws_security_group" "vuln_sg"'):
        inside_sg_block = True

    # Fix SSH open to 0.0.0.0/0
    if inside_sg_block and 'cidr_blocks = ["0.0.0.0/0"]' in stripped and 'from_port   = 22' in tf_lines[tf_lines.index(line)-1]:
        line = line.replace('["0.0.0.0/0"]', '["10.0.0.0/24"]')  # Example: restrict to local network

    # Fix open egress to 0.0.0.0/0
    if inside_sg_block and 'cidr_blocks = ["0.0.0.0/0"]' in stripped and 'egress {' in tf_lines[tf_lines.index(line)-2]:
        line = line.replace('["0.0.0.0/0"]', '["10.0.0.0/24"]')

    # End of block
    if stripped == "}":
        inside_sg_block = False

    new_tf_lines.append(line)

# Write back fixed Terraform file
with open(tf_file, "w") as f:
    f.writelines(new_tf_lines)

print("✅ Terraform main.tf has been updated with AI-based security fixes!") 