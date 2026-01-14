pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Python') {
            steps {
                script {
                    echo '🐍 Configuration de Python...'
                    
                    // Vérifier si Python est déjà installé
                    def pythonCheck = bat(returnStatus: true, script: 'python --version 2>nul')
                    
                    if (pythonCheck != 0) {
                        echo 'Python non trouvé. Installation manuelle requise.'
                        echo 'Veuillez installer Python 3.14.2 depuis https://www.python.org/downloads/'
                        error('Python non installé sur cet agent')
                    } else {
                        echo '✅ Python est déjà installé'
                        bat 'python --version'
                    }
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                bat """
                    @echo off
                    echo === Installation des dépendances ===
                    python --version
                    python -m pip install --upgrade pip
                    python -m pip install selenium webdriver-manager
                    echo ✅ Dépendances installées
                """
            }
        }
        
        stage('Run Tests') {
            steps {
                bat """
                    @echo off
                    echo === Exécution des tests ===
                    python sauce_demo_tests.py
                """
            }
        }
    }
    
    post {
        success {
            echo '✅ Pipeline exécuté avec succès!'
        }
        failure {
            echo '❌ Pipeline a échoué'
        }
        always {
            echo 'Pipeline terminé'
        }
    }
}
