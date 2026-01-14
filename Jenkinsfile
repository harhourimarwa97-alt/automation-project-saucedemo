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
                    // Try to run python; if not present, attempt Chocolatey install, otherwise fail with helpful message
                    def rc = bat(returnStatus: true, script: 'python --version')
                    if (rc != 0) {
                        echo 'Python non trouvé sur cet agent. Tentative d\'installation via Chocolatey...'
                        def chocoRc = bat(returnStatus: true, script: 'choco --version')
                        if (chocoRc == 0) {
                            bat 'choco install -y python'
                            // Re-check python after install
                            def rc2 = bat(returnStatus: true, script: 'python --version')
                            if (rc2 != 0) {
                                error('Python a été installé mais n\'est pas encore disponible dans le PATH. Redémarrez l\'agent ou configurez Python sur l\'agent Jenkins.')
                            }
                            bat 'python -m pip --version'
                        } else {
                            error('Python n\'est pas installé sur cet agent et Chocolatey n\'est pas disponible. Veuillez installer Python sur l\'agent Jenkins ou configurer un outil Python dans Jenkins. Voir: https://www.python.org/downloads/')
                        }
                    } else {
                        bat 'python --version'
                        bat 'python -m pip --version'
                    }
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    echo '📦 Installation des dépendances...'
                    bat 'python -m pip install --upgrade pip'
                    bat 'python -m pip install -r requirements.txt'
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
