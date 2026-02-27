pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out GitHub repository...'
                git branch: 'main', url: 'https://github.com/Gaurvi123456/DEVSECOPS-FLASK-APP.git'
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
                # Run Trivy again after AI fixes
                trivy config --format json --output trivy-report.json .
                
                # Fail pipeline if any HIGH/CRITICAL issues remain
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