pipeline {
    agent {
        docker { 
            image 'python:3.11-slim' // Official Python image
            args '-v /var/run/docker.sock:/var/run/docker.sock' // if you need Docker inside container
        }
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out GitHub repository...'
                git branch: 'main', url: 'https://github.com/Gaurvi123456/DEVSECOPS-FLASK-APP.git'
            }
        }

        stage('Install Trivy') {
            steps {
                echo 'Installing Trivy scanner...'
                sh '''
                apt-get update -y
                apt-get install -y wget
                wget https://github.com/aquasecurity/trivy/releases/download/v0.55.2/trivy_0.55.2_Linux-64bit.deb
                dpkg -i trivy_0.55.2_Linux-64bit.deb
                '''
            }
        }

        stage('Trivy IaC Scan') {
            steps {
                echo 'Running Trivy Infrastructure as Code scan...'
                sh '''
                # Run Trivy and save JSON report
                trivy config --format json --output trivy-report.json .

                # Fail pipeline if HIGH/CRITICAL issues found
                python check_trivy_fail.py trivy-report.json
                '''
            }
        }

        stage('AI Security Remediation') {
            steps {
                echo 'Running AI-based Terraform remediation...'
                sh '''
                # Apply AI remediation to fix vulnerabilities in main.tf
                python ai_remediation.py trivy-report.json
                '''
            }
        }

        stage('Re-run Trivy Scan After AI Fix') {
            steps {
                echo 'Re-running Trivy scan to confirm fixes...'
                sh '''
                trivy config --format json --output trivy-report.json .
                python check_trivy_fail.py trivy-report.json
                '''
            }
        }

        stage('Terraform Plan') {
            steps {
                echo 'Running terraform plan...'
                sh 'cd terraform && terraform init && terraform plan'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
    }
}