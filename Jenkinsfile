pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Gaurvi123456/DEVSECOPS-FLASK-APP.git'
            }
        }

        stage('Trivy IaC Scan') {
            steps {
                bat '''
                trivy config --format json --output trivy-report.json .
                python check_trivy_fail.py trivy-report.json
                '''
            }
        }

        stage('AI Security Remediation') {
            steps {
                bat 'python ai_remediation.py trivy-report.json'
            }
        }

        stage('Re-run Trivy Scan After AI Fix') {
            steps {
                bat '''
                trivy config --format json --output trivy-report.json .
                python check_trivy_fail.py trivy-report.json
                '''
            }
        }

        stage('Terraform Plan') {
            steps {
                bat 'cd terraform && terraform init && terraform plan'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
    }
}