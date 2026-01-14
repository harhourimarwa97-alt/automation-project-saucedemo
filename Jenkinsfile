pipeline {
    agent any
    
    stages {
        stage('Vérifier Python') {
            steps {
                bat """
                    echo "=== Vérification ==="
                    where python
                    python --version
                    pip --version
                """
            }
        }
        
        stage('Récupérer code') {
            steps {
                checkout scm
            }
        }
        
        stage('Installer dépendances') {
            steps {
                bat """
                    echo "Installation des packages..."
                    pip install selenium
                    echo "✅ Selenium installé"
                """
            }
        }
        
        stage('Exécuter tests') {
            steps {
                bat """
                    echo "Exécution des tests..."
                    python sauce_demo_tests.py
                """
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline terminé'
        }
    }
}
