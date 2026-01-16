
🛡️ Tests d'Authentification Selenium avec Python

Ce projet implémente un test automatisé pour valider la robustesse de la gestion des erreurs de connexion sur l'application de démonstration Sauce Demo.

🎯 Objectif Principal

Garantir l'affichage précis des messages d'erreur et la fonctionnalité du mécanisme de fermeture d'erreur lors des tentatives d'authentification échouées.

🧪 Détails du Test

IDNom du TestDescriptionStatut de VérificationT1Gestion des Erreurs de ConnexionVérification des scénarios de connexion échouée (identifiants invalides ou manquants).✅ Validé

📝 Scénarios et Messages d'Erreur Vérifiés

Le script vérifie la présence exacte des messages suivants :

Tentative de ConnexionMessage d'Erreur Attendu❌ Identifiants Invalides"Epic sadface: Username and password do not match any user in this service"👤 Nom d'Utilisateur Manquant"Epic sadface: Username is required"🔑 Mot de Passe Manquant"Epic sadface: Password is required"

💻 Points Techniques Clés

Le script de test met l'accent sur :

1. Localisation d'Éléments : Ciblage précis des champs d'entrée (<input>) et du bouton de connexion.

2. Gestion des Erreurs : Implémentation de mécanismes pour localiser et valider le texte des messages d'erreur dynamiques.

3. Validation d'Interface : Vérification de la fonctionnalité de fermeture du bandeau d'erreur.

⚙️ Prérequis & Installation

ComposantInstallationPythonVersion 3.x recommandée.Seleniumpip install seleniumWebDriverMettre le pilote (e.g., chromedriver) dans le PATH du système ou le spécifier dans le script.

▶️ Exécution

# Exemple de commande d'exécution du script de test
python TestSauceDemo.py
