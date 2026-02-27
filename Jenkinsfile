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
                // Scan current folder safely
                sh 'trivy config .'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
    }
}