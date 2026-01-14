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
                    
                    // Vérifier si python ou py est disponible
                    def pythonCheck = bat(returnStatus: true, script: 'python --version 2>nul')
                    def pyCheck = bat(returnStatus: true, script: 'py --version 2>nul')
                    
                    if (pythonCheck == 0) {
                        echo '✅ Python (commande python) est disponible'
                        env.PYTHON_CMD = 'python'
                    } else if (pyCheck == 0) {
                        echo '✅ Python (commande py) est disponible'
                        env.PYTHON_CMD = 'py'
                    } else {
                        echo 'Python non trouvé. Installation manuelle requise.'
                        echo 'Veuillez installer Python 3.14.2 depuis https://www.python.org/downloads/'
                        error('Python non installé sur cet agent')
                    }
                    
                    // Afficher la version de Python
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
                    ${env.PYTHON_CMD} sauce_demo_tests.py
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
