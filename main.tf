# Comment out AWS provider for local scanning
# provider "aws" {
#   region = "ap-south-1"
# }

# Keep resources as-is (Trivy will still scan them)
resource "aws_security_group" "vuln_sg" {
  name = "vulnerable-sg"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/24"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/24"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["10.0.0.0/24"]
  }
}

resource "aws_instance" "web" {
  ami           = "ami-0f5ee92e2d63afc18"
  instance_type = "t2.micro"
  security_groups = [aws_security_group.vuln_sg.name]

  metadata_options {
    http_tokens = "required"
  }
  root_block_device {
    encrypted = true
  }
  root_block_device {
    encrypted = true
  }
  root_block_device {
    encrypted = true
  }

    user_data = <<-EOF
              #!/bin/bash
              docker run -d -p 80:3000 your-dockerhub-username/app-image
              EOF

  tags = {
    Name = "DevOps-Assignment-VM"
  }
}