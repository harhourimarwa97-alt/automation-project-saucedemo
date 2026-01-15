"""
🚀 TESTS AUTOMATISÉS SAUCEDEMO - VERSION FINALE
📝 Tests de connexion avec Selenium Python
👨‍💻 Pour débutants - Simple et clair
✨ Inclut tous les tests + test de performance
"""

import json
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class TestSauceDemo:
    def __init__(self):
        """🎯 INITIALISATION - Charger les données de test"""
        self.driver = None  # Navigateur web
        self.wait = None    # Attente
        self.resultats = []  # Stocker les résultats
        
        # 📁 Charger les données depuis le fichier JSON
        try:
            with open('ConnexionError.json', 'r') as file:
                self.test_data = json.load(file)
            print("✅ Données chargées avec succès")
        except FileNotFoundError:
            print("❌ ERREUR: Fichier 'ConnexionError.json' non trouvé!")
            print("💡 Créez le fichier JSON dans le même dossier")
            exit(1)
    
    def ouvrir_chrome(self):
        """🖥️ OUVRE UN NAVIGATEUR CHROME"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  # Plein écran
        self.wait = WebDriverWait(self.driver, 10)  # Attendre max 10 sec
        print("🌐 Chrome ouvert")
    
    def ouvrir_edge(self):
        """🖥️ OUVRE UN NAVIGATEUR EDGE"""
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        print("🌐 Edge ouvert")
    
    def fermer_navigateur(self):
        """❌ FERME LE NAVIGATEUR"""
        if self.driver:
            self.driver.quit()
            print("🔴 Navigateur fermé")
            self.driver = None
            self.wait = None
    
    def aller_site(self):
        """🌍 ALLER SUR LE SITE SAUCEDEMO"""
        self.driver.get("https://www.saucedemo.com/")
        print("  📍 Site ouvert: saucedemo.com")
    
    def se_connecter(self, username, password):
        """🔐 SE CONNECTER AVEC IDENTIFIANTS"""
        # Trouver les champs de connexion
        champ_user = self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        champ_pass = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
        
        # Effacer et remplir
        champ_user.clear()
        champ_pass.clear()
        
        champ_user.send_keys(username)
        champ_pass.send_keys(password)
        champ_pass.send_keys(Keys.RETURN)  # Appuyer sur Entrée
        
        print(f"  🔑 Test avec: {username} / {password}")
    
    def verifier_erreur(self, message_attendu):
        """⚠️ VÉRIFIER LE MESSAGE D'ERREUR"""
        try:
            # Trouver le message d'erreur
            erreur = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container"))
            )
            message_obtenu = erreur.text.strip()
            
            # Vérifier si le message est correct
            if message_attendu == message_obtenu:
                print(f"  ✅ Message correct: '{message_obtenu}'")
                return True
            else:
                print(f"  ❌ Message incorrect")
                print(f"     Attendu: '{message_attendu}'")
                print(f"     Reçu: '{message_obtenu}'")
                return False
        except Exception as e:
            print(f"  ❌ Erreur: {e}")
            return False
    
    def fermer_message_erreur(self):
        """❌ TESTER LE BOUTON DE FERMETURE"""
        try:
            # Trouver le bouton X
            bouton_x = self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "error-button"))
            )
            bouton_x.click()  # Cliquer
            
            # Attendre que le message disparaisse
            time.sleep(1)
            print("  ✅ Bouton fermeture fonctionne")
            return True
        except Exception as e:
            print(f"  ❌ Erreur bouton: {e}")
            return False
    
    # ==============================================
    # 🧪 TESTS INDIVIDUELS
    # ==============================================
    
    def test1_connexion_ok_chrome(self):
        """🧪 TEST 1: CONNEXION RÉUSSIE AVEC CHROME"""
        test_nom = "Chrome - Connexion réussie"
        print("\n" + "="*60)
        print(f"🧪 TEST 1: {test_nom}")
        print("="*60)
        
        try:
            # 1. Ouvrir Chrome
            self.ouvrir_chrome()
            
            # 2. Aller sur le site
            self.aller_site()
            
            # 3. Prendre les données de test
            data = self.test_data["nominal"]
            
            # 4. Se connecter
            self.se_connecter(data["username"], data["password"])
            
            # 5. Vérifier la connexion
            self.wait.until(EC.url_contains("inventory"))
            print("  ✅ CONNEXION RÉUSSIE!")
            
            # 6. Prendre une capture d'écran
            self.driver.save_screenshot("test1_ok_chrome.png")
            print("  📸 Capture sauvegardée")
            
            self.resultats.append((test_nom, True, "✅ SUCCÈS"))
            return True
            
        except Exception as e:
            print(f"  ❌ ÉCHEC: {e}")
            self.resultats.append((test_nom, False, "❌ ÉCHEC"))
            return False
            
        finally:
            # 7. Fermer le navigateur
            self.fermer_navigateur()
            time.sleep(1)
    
    def test2_connexion_ok_edge(self):
        """🧪 TEST 2: CONNEXION RÉUSSIE AVEC EDGE"""
        test_nom = "Edge - Connexion réussie"
        print("\n" + "="*60)
        print(f"🧪 TEST 2: {test_nom}")
        print("="*60)
        
        try:
            # 1. Ouvrir Edge
            self.ouvrir_edge()
            
            # 2. Aller sur le site
            self.aller_site()
            
            # 3. Prendre les données de test
            data = self.test_data["nominal"]
            
            # 4. Se connecter
            self.se_connecter(data["username"], data["password"])
            
            # 5. Vérifier la connexion
            self.wait.until(EC.url_contains("inventory"))
            print("  ✅ CONNEXION RÉUSSIE!")
            
            # 6. Prendre une capture d'écran
            self.driver.save_screenshot("test2_ok_edge.png")
            print("  📸 Capture sauvegardée")
            
            self.resultats.append((test_nom, True, "✅ SUCCÈS"))
            return True
            
        except Exception as e:
            print(f"  ❌ ÉCHEC: {e}")
            self.resultats.append((test_nom, False, "❌ ÉCHEC"))
            return False
            
        finally:
            # 7. Fermer le navigateur
            self.fermer_navigateur()
            time.sleep(1)
    
    def test3_erreur_utilisateur_invalide(self):
        """🧪 TEST 3: ERREUR - MAUVAIS UTILISATEUR"""
        test_nom = "Erreur - Utilisateur invalide"
        print("\n" + "="*60)
        print(f"🧪 TEST 3: {test_nom}")
        print("="*60)
        
        try:
            # 1. Ouvrir Chrome
            self.ouvrir_chrome()
            
            # 2. Aller sur le site
            self.aller_site()
            
            # 3. Prendre les données du test
            test = self.test_data["erreur_connexion"][0]
            
            # 4. Tenter la connexion (doit échouer)
            self.se_connecter(test["username"], test["password"])
            
            # 5. Vérifier le message d'erreur
            ok_erreur = self.verifier_erreur(test["message_erreur"])
            
            # 6. Tester le bouton de fermeture
            ok_bouton = self.fermer_message_erreur()
            
            # 7. Capture d'écran
            self.driver.save_screenshot("test3_mauvais_user.png")
            print("  📸 Capture sauvegardée")
            
            resultat_final = ok_erreur and ok_bouton
            statut = "✅ SUCCÈS" if resultat_final else "❌ ÉCHEC"
            self.resultats.append((test_nom, resultat_final, statut))
            return resultat_final
            
        except Exception as e:
            print(f"  ❌ ERREUR: {e}")
            self.resultats.append((test_nom, False, "❌ ÉCHEC"))
            return False
            
        finally:
            # 8. Fermer le navigateur
            self.fermer_navigateur()
            time.sleep(1)
    
    def test4_erreur_sans_username(self):
        """🧪 TEST 4: ERREUR - SANS NOM D'UTILISATEUR"""
        test_nom = "Erreur - Sans nom d'utilisateur"
        print("\n" + "="*60)
        print(f"🧪 TEST 4: {test_nom}")
        print("="*60)
        
        try:
            # 1. Ouvrir Chrome
            self.ouvrir_chrome()
            
            # 2. Aller sur le site
            self.aller_site()
            
            # 3. Prendre les données du test
            test = self.test_data["erreur_connexion"][1]
            
            # 4. Tenter la connexion (doit échouer)
            self.se_connecter(test["username"], test["password"])
            
            # 5. Vérifier le message d'erreur
            ok_erreur = self.verifier_erreur(test["message_erreur"])
            
            # 6. Tester le bouton de fermeture
            ok_bouton = self.fermer_message_erreur()
            
            # 7. Capture d'écran
            self.driver.save_screenshot("test4_sans_username.png")
            print("  📸 Capture sauvegardée")
            
            resultat_final = ok_erreur and ok_bouton
            statut = "✅ SUCCÈS" if resultat_final else "❌ ÉCHEC"
            self.resultats.append((test_nom, resultat_final, statut))
            return resultat_final
            
        except Exception as e:
            print(f"  ❌ ERREUR: {e}")
            self.resultats.append((test_nom, False, "❌ ÉCHEC"))
            return False
            
        finally:
            # 8. Fermer le navigateur
            self.fermer_navigateur()
            time.sleep(1)
    
    def test5_erreur_sans_password(self):
        """🧪 TEST 5: ERREUR - SANS MOT DE PASSE"""
        test_nom = "Erreur - Sans mot de passe"
        print("\n" + "="*60)
        print(f"🧪 TEST 5: {test_nom}")
        print("="*60)
        
        try:
            # 1. Ouvrir Chrome
            self.ouvrir_chrome()
            
            # 2. Aller sur le site
            self.aller_site()
            
            # 3. Prendre les données du test
            test = self.test_data["erreur_connexion"][2]
            
            # 4. Tenter la connexion (doit échouer)
            self.se_connecter(test["username"], test["password"])
            
            # 5. Vérifier le message d'erreur
            ok_erreur = self.verifier_erreur(test["message_erreur"])
            
            # 6. Tester le bouton de fermeture
            ok_bouton = self.fermer_message_erreur()
            
            # 7. Capture d'écran
            self.driver.save_screenshot("test5_sans_password.png")
            print("  📸 Capture sauvegardée")
            
            resultat_final = ok_erreur and ok_bouton
            statut = "✅ SUCCÈS" if resultat_final else "❌ ÉCHEC"
            self.resultats.append((test_nom, resultat_final, statut))
            return resultat_final
            
        except Exception as e:
            print(f"  ❌ ERREUR: {e}")
            self.resultats.append((test_nom, False, "❌ ÉCHEC"))
            return False
            
        finally:
            # 8. Fermer le navigateur
            self.fermer_navigateur()
            time.sleep(1)
    
    def test6_utilisateur_bloque(self):
        """🧪 TEST 6: UTILISATEUR BLOQUÉ"""
        test_nom = "Utilisateur bloqué"
        print("\n" + "="*60)
        print(f"🧪 TEST 6: {test_nom}")
        print("="*60)
        
        try:
            # 1. Ouvrir Chrome
            self.ouvrir_chrome()
            
            # 2. Aller sur le site
            self.aller_site()
            
            # 3. Tenter connexion avec utilisateur bloqué
            self.se_connecter("locked_out_user", "secret_sauce")
            
            # 4. Vérifier le message d'erreur
            message = "Epic sadface: Sorry, this user has been locked out."
            ok_erreur = self.verifier_erreur(message)
            
            # 5. Tester le bouton de fermeture
            ok_bouton = self.fermer_message_erreur()
            
            # 6. Capture d'écran
            self.driver.save_screenshot("test6_user_bloque.png")
            print("  📸 Capture sauvegardée")
            
            resultat_final = ok_erreur and ok_bouton
            statut = "✅ SUCCÈS" if resultat_final else "❌ ÉCHEC"
            self.resultats.append((test_nom, resultat_final, statut))
            return resultat_final
            
        except Exception as e:
            print(f"  ❌ ERREUR: {e}")
            self.resultats.append((test_nom, False, "❌ ÉCHEC"))
            return False
            
        finally:
            # 7. Fermer le navigateur
            self.fermer_navigateur()
            time.sleep(1)
    
    def test7_performance_connexion(self):
        """🧪 TEST 7: PERFORMANCE DE CONNEXION"""
        test_nom = "Test de performance"
        print("\n" + "="*60)
        print(f"🧪 TEST 7: {test_nom}")
        print("="*60)
        
        try:
            # 1. Ouvrir Chrome
            self.ouvrir_chrome()
            
            # 2. Mesurer le temps de chargement initial
            print("  ⏱️  Mesure du temps de chargement...")
            start_time = time.time()
            self.aller_site()
            load_time = time.time() - start_time
            
            # Afficher les résultats de chargement
            print(f"  📊 Temps de chargement de la page: {load_time:.2f} secondes")
            
            if load_time < 3:
                print("  ✅ EXCELLENT: Chargement très rapide")
                load_score = 3
            elif load_time < 5:
                print("  ✅ BON: Chargement dans les normes")
                load_score = 2
            else:
                print("  ⚠️  ATTENTION: Chargement lent")
                load_score = 1
            
            # 3. Mesurer le temps de connexion
            print("\n  ⏱️  Mesure du temps de connexion...")
            data = self.test_data["nominal"]
            
            # Démarrer le chrono
            start_time = time.time()
            
            # Remplir le formulaire
            champ_user = self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
            champ_pass = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
            
            champ_user.clear()
            champ_pass.clear()
            
            champ_user.send_keys(data["username"])
            champ_pass.send_keys(data["password"])
            champ_pass.send_keys(Keys.RETURN)
            
            # Attendre la redirection
            self.wait.until(EC.url_contains("inventory"))
            
            # Arrêter le chrono
            login_time = time.time() - start_time
            
            # Afficher les résultats de connexion
            print(f"  📊 Temps total de connexion: {login_time:.2f} secondes")
            
            if login_time < 2:
                print("  ✅ EXCELLENT: Connexion très rapide")
                login_score = 3
            elif login_time < 4:
                print("  ✅ BON: Connexion dans les normes")
                login_score = 2
            else:
                print("  ⚠️  ATTENTION: Connexion lente")
                login_score = 1
            
            # 4. Calculer le score global
            total_score = load_score + login_score
            score_max = 6
            
            print(f"\n  📈 SCORE DE PERFORMANCE: {total_score}/{score_max}")
            
            if total_score >= 5:
                print("  🏆 PERFORMANCE EXCELLENTE!")
                performance_ok = True
            elif total_score >= 3:
                print("  👍 PERFORMANCE SATISFAISANTE")
                performance_ok = True
            else:
                print("  ⚠️  PERFORMANCE À AMÉLIORER")
                performance_ok = False
            
            # 5. Enregistrer les résultats dans un fichier
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("performance_results.txt", "a") as f:
                f.write(f"\n{'='*40}\n")
                f.write(f"TEST DE PERFORMANCE - {timestamp}\n")
                f.write(f"{'='*40}\n")
                f.write(f"Temps de chargement: {load_time:.2f} secondes\n")
                f.write(f"Temps de connexion: {login_time:.2f} secondes\n")
                f.write(f"Score: {total_score}/{score_max}\n")
                f.write(f"Résultat: {'PASS' if performance_ok else 'FAIL'}\n")
            
            print("  💾 Résultats sauvegardés dans 'performance_results.txt'")
            
            # 6. Prendre une capture d'écran
            self.driver.save_screenshot("test7_performance.png")
            print("  📸 Capture d'écran sauvegardée")
            
            statut = "✅ SUCCÈS" if performance_ok else "❌ ÉCHEC"
            self.resultats.append((test_nom, performance_ok, statut))
            return performance_ok
            
        except Exception as e:
            print(f"  ❌ ERREUR pendant le test de performance: {e}")
            self.resultats.append((test_nom, False, "❌ ÉCHEC"))
            return False
            
        finally:
            # 7. Fermer le navigateur
            self.fermer_navigateur()
            time.sleep(1)
    
    def lancer_tous_les_tests(self):
        """🚀 LANCER TOUS LES TESTS"""
        print("\n" + "🚀" * 25)
        print("🚀 DÉBUT DES TESTS SAUCEDEMO 🚀")
        print("🚀" * 25)
        
        # 📋 Liste de tous les tests
        liste_tests = [
            self.test1_connexion_ok_chrome,
            self.test2_connexion_ok_edge,
            self.test3_erreur_utilisateur_invalide,
            self.test4_erreur_sans_username,
            self.test5_erreur_sans_password,
            self.test6_utilisateur_bloque,
            self.test7_performance_connexion,
        ]
        
        # 🔄 Exécuter chaque test
        for i, fonction_test in enumerate(liste_tests, 1):
            print(f"\n{'📌' * 25}")
            print(f"🔍 Test {i}/{len(liste_tests)}")
            print(f"{'📌' * 25}")
            
            try:
                # Exécuter le test
                resultat = fonction_test()
                
                # Afficher le résultat immédiat
                if resultat:
                    print(f"\n  🎉 RÉSULTAT IMMÉDIAT: SUCCÈS ✅")
                else:
                    print(f"\n  😞 RÉSULTAT IMMÉDIAT: ÉCHEC ❌")
                
                # Pause de 2 secondes entre les tests
                time.sleep(2)
                
            except Exception as e:
                print(f"\n  ❌ ERREUR: {e}")
        
        # 📊 Afficher le résumé final
        self.afficher_resume_tableau()
    
    def afficher_resume_tableau(self):
        """📊 AFFICHER LE RÉSUMÉ EN TABLEAU + STATISTIQUES"""
        
        print("\n" + "━" * 65)
        print(f"{'N°':<3} {'TEST':<40} {'STATUT':<12} {'RÉSULTAT':<10}")
        print("━" * 65)
        
        # Afficher chaque résultat dans le tableau
        for i, (nom_test, resultat, statut) in enumerate(self.resultats, 1):
            emoji_resultat = "✅" if resultat else "❌"
            print(f"{i:<3} {nom_test:<40} {statut:<12} {emoji_resultat:<10}")
        
        print("━" * 65)
        
        # 📈 STATISTIQUES GLOBALES
        print("\n" + "📈" * 15)
        print("📈 STATISTIQUES GLOBALES")
        print("📈" * 15)
        
        total_tests = len(self.resultats)
        tests_reussis = sum(1 for _, resultat, _ in self.resultats if resultat)
        tests_echoues = total_tests - tests_reussis
        taux_reussite = (tests_reussis / total_tests * 100) if total_tests > 0 else 0
        
        print(f"\n┌{'─'*40}┐")
        print(f"│ 📋 TOTAL DES TESTS EXÉCUTÉS : {total_tests:2d}        │")
        print(f"│ ✅ TESTS RÉUSSIS           : {tests_reussis:2d}        │")
        print(f"│ ❌ TESTS ÉCHOUÉS           : {tests_echoues:2d}        │")
        print(f"│ 📊 TAUX DE RÉUSSITE        : {taux_reussite:6.1f}%     │")
        print(f"└{'─'*40}┘")
        
        # 📅 DATE D'EXÉCUTION
        print("\n" + "=" * 60)
        print(f"⏱️  Date d'exécution: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)
        
        # Message final
        if tests_reussis == total_tests:
            print("\n🎉🎉🎉 FÉLICITATIONS ! TOUS LES TESTS SONT RÉUSSIS ! 🎉🎉🎉")
        elif taux_reussite >= 80:
            print(f"\n👍 EXCELLENT ! {tests_reussis}/{total_tests} tests réussis")
        else:
            print(f"\n⚠️  {tests_echoues} test(s) échoué(s). Vérification nécessaire.")
        
        print("\n📁 Fichiers générés:")
        fichiers = [
            "test1_ok_chrome.png", "test2_ok_edge.png", 
            "test3_mauvais_user.png", "test4_sans_username.png",
            "test5_sans_password.png", "test6_user_bloque.png",
            "test7_performance.png", "performance_results.txt"
        ]
        for fichier in fichiers:
            print(f"  📄 {fichier}")

# ==============================================
# 🚀 POINT D'ENTRÉE PRINCIPAL
# ==============================================

if __name__ == "__main__":
    print("\n🔧" * 25)
    print("🔧 TESTS AUTOMATISÉS SAUCEDEMO")
    print("🔧 7 tests complets incluant performance")
    print("🔧" * 25)
    
    print("\n📋 TESTS INCLUS:")
    print("  1. ✅ Connexion réussie (Chrome)")
    print("  2. ✅ Connexion réussie (Edge)")
    print("  3. ❌ Erreur - Utilisateur invalide")
    print("  4. ❌ Erreur - Sans nom d'utilisateur")
    print("  5. ❌ Erreur - Sans mot de passe")
    print("  6. ❌ Utilisateur bloqué")
    print("  7. ⚡ Test de performance")
    
    print("\n⚠️  IMPORTANT: Assurez-vous d'avoir:")
    print("  1. Chrome et Edge installés")
    print("  2. ChromeDriver et EdgeDriver téléchargés")
    print("  3. Fichier 'ConnexionError.json' dans le dossier")
    
    print("\n⏳ Démarrage dans 3 secondes...")
    time.sleep(3)
    
    # Créer l'objet de test
    testeur = TestSauceDemo()
    
    try:
        # Lancer tous les tests
        testeur.lancer_tous_les_tests()
        
    except KeyboardInterrupt:
        print("\n\n⏹️  Tests interrompus par l'utilisateur")
        
    except Exception as e:
        print(f"\n🔥 ERREUR: {e}")
        
    finally:
        # Fermer le navigateur si encore ouvert
        if testeur.driver:
            testeur.fermer_navigateur()
        
        print("\n👋 Programme terminé.")
