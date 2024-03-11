pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/zayn-shayq/mlop_class_task_3_i2008955.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Assuming Python dependencies
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Execute test.py') {
            steps {
                sh 'python test.py'
            }
        }

        stage('Deploying') {
            steps {
                script {
                    if (env.BRANCH_NAME == 'main') {
                        echo 'Deploying to production'
                    } else {
                        echo 'Deploying to UAT'
                    }
                }
            }
        }
    }
}
