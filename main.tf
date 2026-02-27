provider "aws" {
  region = "ap-south-1"
}

resource "aws_security_group" "vuln_sg" {
  name = "vulnerable-sg"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # ❌ INTENTIONAL VULNERABILITY (SSH open to world)
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "web" {
  ami           = "ami-0f5ee92e2d63afc18"
  instance_type = "t2.micro"
  security_groups = [aws_security_group.vuln_sg.name]

  user_data = <<-EOF
              #!/bin/bash
              docker run -d -p 80:3000 your-dockerhub-username/app-image
              EOF

  tags = {
    Name = "DevOps-Assignment-VM"
  }
}