pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('List Files') {
            steps {
                bat """
                    @echo off
                    echo === Structure du projet ===
                    dir /S /B *.py
                    echo.
                    dir /B
                    echo.
                    cd selenium_tests
                    dir /B
                """
            }
        }
        
        stage('Setup Python') {
            steps {
                script {
                    echo '🐍 Configuration de Python...'
                    
                    // Essayer différentes commandes Python
                    def pythonCheck = bat(returnStatus: true, script: 'python --version 2>nul')
                    def pyCheck = bat(returnStatus: true, script: 'py --version 2>nul')
                    
                    if (pythonCheck == 0) {
                        echo '✅ Python (python) est disponible'
                        env.PYTHON_CMD = 'python'
                    } else if (pyCheck == 0) {
                        echo '✅ Python (py) est disponible'
                        env.PYTHON_CMD = 'py'
                    } else {
                        echo 'Python non trouvé. Installation manuelle requise.'
                        error('Python non installé sur cet agent')
                    }
                    
                    bat "${env.PYTHON_CMD} --version"
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                bat """
                    @echo off
                    echo === Installation des dépendances ===
                    ${env.PYTHON_CMD} --version
                    ${env.PYTHON_CMD} -m pip install --upgrade pip
                    ${env.PYTHON_CMD} -m pip install selenium webdriver-manager
                    echo ✅ Dépendances installées
                """
            }
        }
        
        stage('Run Tests') {
            steps {
                bat """
                    @echo off
                    echo === Exécution des tests ===
                    cd selenium_tests
                    ${env.PYTHON_CMD} ConnexionErrorHandling.py
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
