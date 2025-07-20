pipeline {
    agent any
    stages {
        stage('Checkout Dev Code') {
            steps {
                checkout scm // Checks out the 'dev' branch code
            }
        }
        stage('Build Dev') {
            steps {
                echo 'Building application for dev environment...'
                // Add your dev-specific build commands here
            }
        }
        stage('Run Dev Tests') {
            steps {
                echo 'Running tests for dev environment...'
                // Add your dev-specific test commands here
            }
        }
        stage('Deploy to Dev') {
            steps {
                echo 'Deploying to dev environment (e.g., dev server, QA)...'
                // Add your dev-specific deployment commands here
            }
        }
    }
    post {
        always {
            echo 'Dev pipeline finished.'
        }
        failure {
            echo 'Dev pipeline failed!'
        }
    }
}
