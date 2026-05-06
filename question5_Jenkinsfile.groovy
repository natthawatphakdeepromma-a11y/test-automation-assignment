pipeline {
    agent any

    stages {
        stage('Checkout Code From Git') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/natthawatphakdeepromma-a11y/test-automation-assignment.git'
            }
        }

        stage('Run Test Automate') {
            steps {
                sh '''
                    pip3 install -r requirements.txt
                    python3 -m pytest question2_login_automation.py question3_api_test.py -v --junitxml=result.xml
                '''
            }
        }

        stage('Send Result To Jenkins') {
            steps {
                junit 'result.xml'
            }
        }
    }
}
