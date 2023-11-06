import subprocess
import Calcultrice
import Convertisseur
import dé
import generateur_mdp
import manoir_hanté
import tests
import x3
import chrome

chemin_cal = "./cal_launcher.bat"
chemin_conv = "./conv_launcher.bat"
chemin_de = "./de_launcher.bat"
chemin_mdp = "./mdp_launcher.bat"
chemin_mh = "./mh_launcher.bat"
chemin_test = "./tests_launcher.bat"
chemin_x3 = "./x3_launcher.bat"
chemin_nav = "./chrome_launcher.bat"

print("Quel projet voulez-vous lancer ? (entrer les lettre correspondante)")
print("Calculatrice : cal")
print("Convertisseur : conv")
print("Dé : de")
print("Générateur de mot de passe : mdp")
print("Jeu de manoir hanté : mh")
print("Fichier de tests : test")
print("Jeu de 3 : x3")
print("Chrome de wish : nav")

quel = input()

if quel == "cal":
    Calcultrice.launch_cal
elif quel == "conv":
    Convertisseur.launch_cv
elif quel == "de":
    dé.dé
elif quel == "mdp":
    subprocess.call(chemin_mdp, shell=True)
elif quel == "mh":
    manoir_hanté.manoirHanté
elif quel == "test":
    tests.launch_tests
elif quel == "x3":
    x3.x3
elif quel == "nav":
    chrome.launch_nav
else:
    print("Veuillez entrer des lettres valides")
    exit()