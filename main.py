import Calcultrice
import Convertisseur
import dé
import generateur_mdp
import manoir_hanté
import tests
import x3
import chrome

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
    generateur_mdp.launch_mdp
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