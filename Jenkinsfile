pipeline {
    agent any

    environment {
        // Optional: set environment variables if needed
        PATH = "/usr/local/bin:${env.PATH}"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Checking out GitHub repository...'
                // Explicitly use main branch
                git branch: 'main', url: 'https://github.com/Gaurvi123456/DEVSECOPS-FLASK-APP.git'
            }
        }

        stage('Trivy IaC Scan') {
            steps {
                echo 'Running Trivy Infrastructure as Code scan...'
                // Run Trivy locally in the repo folder
                sh 'trivy iac --exit-code 0 .'
                // --exit-code 0 ensures Jenkins doesn't fail the build, you can remove if you want it to fail on vulnerabilities
            }
        }
    }

    post {
        success {
            echo 'Trivy scan completed successfully ✅'
        }
        failure {
            echo 'Pipeline finished with errors ❌'
        }
        always {
            echo 'Pipeline finished!'
        }
    }
}