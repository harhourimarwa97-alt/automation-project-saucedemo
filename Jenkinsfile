pipeline {
    agent any
    
    parameters {
        choice(
            name: 'BROWSER',
            choices: ['chrome', 'edge', 'all'],
            description: 'Select browser to test'
        )
        booleanParam(
            name: 'SEND_EMAIL',
            defaultValue: true,
            description: 'Send email report'
        )
        string(
            name: 'EMAIL_RECIPIENTS',
            defaultValue: 'qa-team@company.com',
            description: 'Email recipients'
        )
    }
    
    environment {
        PROJECT_DIR = "${WORKSPACE}"
        REPORTS_DIR = "${WORKSPACE}/reports"
        SCREENSHOTS_DIR = "${WORKSPACE}/screenshots"
    }
    
    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()  // Seulement au début, pas dans dir()
            }
        }
        
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Environment') {
            steps {
                sh '''
                    mkdir -p ${REPORTS_DIR}
                    mkdir -p ${SCREENSHOTS_DIR}
                    python3 -m venv venv
                '''
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '''
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    sh """
                        source venv/bin/activate
                        pytest sauce_demo_tests.py --browser=${params.BROWSER} \
                            --junitxml=${REPORTS_DIR}/test-results.xml \
                            --html=${REPORTS_DIR}/report.html \
                            --screenshot-dir=${SCREENSHOTS_DIR}
                    """
                }
            }
        }
        
        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: 'reports/**,screenshots/**'
                junit 'reports/test-results.xml'
                publishHTML([
                    target: [
                        reportDir: 'reports',
                        reportFiles: 'report.html',
                        reportName: 'HTML Report'
                    ]
                ])
            }
        }
    }
    
    post {
        always {
            sh 'rm -rf venv || true'  // Cleanup
        }
        success {
            script {
                if (params.SEND_EMAIL) {
                    emailext(
                        subject: "✅ Build ${env.BUILD_NUMBER} Success",
                        body: "See report: ${env.BUILD_URL}HTML_Report/",
                        to: params.EMAIL_RECIPIENTS
                    )
                }
            }
        }
        failure {
            script {
                if (params.SEND_EMAIL) {
                    emailext(
                        subject: "❌ Build ${env.BUILD_NUMBER} Failed",
                        body: "Check logs: ${env.BUILD_URL}console",
                        to: params.EMAIL_RECIPIENTS
                    )
                }
            }
        }
    }
}
