pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out GitHub repository...'
                git 'https://github.com/Gaurvi123456/DEVSECOPS-FLASK-APP.git'
            }
        }

        stage('Trivy IaC Scan') {
            steps {
                echo 'Running Trivy Infrastructure as Code scan...'
                sh 'trivy iac .'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
    }
}