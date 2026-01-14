pipeline {
    agent any
    
    tools {
        // Configure Python in Jenkins Global Tool Configuration first
        python('Python3')
    }
    
    stages {
        // Étape 1: Récupération du code
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        // Étape 2: Installation des dépendances
        stage('Install Dependencies') {
            steps {
                bat """
                    python -m pip install --upgrade pip
                    pip install selenium webdriver-manager pytest
                """
            }
        }
        
        // Étape 3: Exécution des tests
        stage('Run Tests') {
            steps {
                bat """
                    python -m pytest tests/ -v
                """
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline terminé'
        }
        success {
            echo '✅ Tous les tests ont réussi!'
        }
        failure {
            echo '❌ Certains tests ont échoué!'
        }
    }
}
