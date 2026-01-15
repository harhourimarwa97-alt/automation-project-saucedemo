pipeline {
    agent any
    
    stages {
        stage('Install Python') {
            steps {
                script {
                    echo '📥 Installation de Python...'
                    
                    bat """
                        echo "Vérification de l'installation de Python..."
                        
                        # Si Python n'est pas installé, le télécharger et l'installer
                        python --version 2>nul
                        if errorlevel 1 (
                            echo "Python non détecté, tentative d'installation..."
                            
                            # Télécharger Python (version spécifique)
                            curl -o python-installer.exe https://www.python.org/ftp/python/3.14.2/python-3.14.2-amd64.exe
                            
                            # Installer Python silencieusement
                            python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
                            
                            # Attendre l'installation
                            timeout /t 60
                            
                            # Vérifier l'installation
                            python --version || echo "Redémarrez l'agent après installation"
                        ) else (
                            echo "✅ Python déjà installé"
                        )
                    """
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                bat """
                    python --version
                    pip install selenium
                    python sauce_demo_tests.py
                """
            }
        }
    }
}