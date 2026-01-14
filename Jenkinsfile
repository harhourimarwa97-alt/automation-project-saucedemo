stage('Install Python') {
    steps {
        script {
            echo '📥 Installation de Python...'
            
            bat """
                echo "Vérification de l'installation de Python..."
                
                rem Vérifier si Python est installé
                python --version 2>nul
                if errorlevel 1 (
                    echo "Python non détecté, tentative d'installation..."
                    
                    rem Télécharger Python (version spécifique)
                    curl -o python-installer.exe https://www.python.org/ftp/python/3.14.2/python-3.14.2-amd64.exe
                    
                    rem Installer Python silencieusement
                    echo "Installation de Python, cela peut prendre quelques minutes..."
                    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
                    
                    rem Attendre un peu
                    timeout /t 30 /nobreak
                    
                    rem Essayer avec le chemin par défaut
                    if exist "C:\\Program Files\\Python314\\python.exe" (
                        set "PYTHON_PATH=C:\\Program Files\\Python314"
                    ) else if exist "C:\\Python314\\python.exe" (
                        set "PYTHON_PATH=C:\\Python314"
                    ) else (
                        echo "Impossible de trouver Python après installation."
                        exit 1
                    )
                    
                    rem Utiliser le chemin complet pour vérifier l'installation
                    "%PYTHON_PATH%\\python.exe" --version
                    if errorlevel 1 (
                        echo "Échec de l'installation de Python."
                        exit 1
                    )
                    
                    rem Ajouter Python au PATH de cette session
                    set PATH=%PYTHON_PATH%;%PYTHON_PATH%\\Scripts;%PATH%
                    
                    echo "✅ Python installé avec succès"
                ) else (
                    echo "✅ Python déjà installé"
                )
            """
        }
    }
}
