pipeline {
    agent any

    stages {

        stage('Pytest') {
            steps {
                sh '''
                cd application
                . venv/bin/activate
                pytest
                '''
            }
        }

        stage('Bandit') {
            steps {
                sh '''
                cd application
                . venv/bin/activate
                bandit -r app.py database.py tests/
                '''
            }
        }

        stage('Dependency Audit') {
            steps {
                sh '''
                cd application
                . venv/bin/activate
                pip-audit
                '''
            }
        }
    }
}
