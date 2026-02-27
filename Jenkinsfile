pipeline {
    agent any

    environment {
        TF_DIR = "."  // Terraform code directory
        TRIVY_SEVERITY = "CRITICAL,HIGH" // Fail on high & critical vulnerabilities
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo "Checking out GitHub repository..."
                git branch: 'main', url: 'https://github.com/Gaurvi123456/DEVSECOPS-FLASK-APP.git'
            }
        }

        stage('Terraform Init') {
            steps {
                echo "Initializing Terraform..."
                dir("${TF_DIR}") {
                    sh 'terraform init'
                }
            }
        }

        stage('Terraform Plan') {
            steps {
                echo "Running Terraform plan..."
                dir("${TF_DIR}") {
                    sh 'terraform plan -out=tfplan.out'
                }
            }
        }

        stage('Trivy IaC Scan') {
            steps {
                echo "Scanning Terraform code with Trivy..."
                dir("${TF_DIR}") {
                    sh """
                        trivy config --severity ${TRIVY_SEVERITY} .
                    """
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully! No critical/high vulnerabilities found."
        }
        failure {
            echo "Pipeline failed due to detected vulnerabilities!"
        }
    }
}