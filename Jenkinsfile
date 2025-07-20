pipeline {
    agent any
    stages {
        stage('Checkout Master Code') {
            steps {
                checkout scm // Checks out the 'Master' branch code
            }
        }
        stage('Build Master') {
            steps {
                echo 'Building application for Master environment...'
                // Add your Master-specific build commands here
            }
        }
        stage('Run Master Tests') {
            steps {
                echo 'Running tests for Master environment...'
                // Add your Master-specific test commands here
            }
        }
        stage('Deploy to Master') {
            steps {
                echo 'Deploying to Master environment (e.g., Master server, QA)...'
                // Add your Master-specific deployment commands here
            }
        }
    }
    post {
        always {
            echo 'Master pipeline finished.'
        }
        failure {
            echo 'Master pipeline failed!'
        }
    }
}
