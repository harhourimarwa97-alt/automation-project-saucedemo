pipeline {
    agent any
    
    parameters {
        choice(
            name: 'BROWSER',
            choices: ['chrome', 'edge'],
            description: 'Select browser to test'
        )
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Verify Python') {
            steps {
                script {
                    echo '✅ Vérification de Python...'
                    bat 'python --version'
                    bat 'pip --version'
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    echo '📦 Installation des dépendances...'
                    bat 'pip install selenium webdriver-manager'
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    echo '🧪 Exécution des tests...'
                    bat 'python sauce_demo_tests.py'
                }
            }
        }
        
        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: '*.png, *.txt, *.log', fingerprint: true
            }
        }
    }
}
