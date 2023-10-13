def longueur():
    print("Convertisseur d'unités de mesure de longueur")

def energie():
    print("Convertisseur d'unités de mesure d'énergie")

def vitesse():
    print("Convertisseur d'unités de vitesse")

def surprise():
    print("UWU")
    exit()

def depart():
    print("Bienvenue dans mon convertisseur d'unités")
    departInput = input("Pour convertir une unité de longueur, écrire L, pour l'énergie, E et pour quitter, Q")
    if departInput == "L":longueur()
    elif departInput == "E":energie()
    elif departInput == "V":vitesse()
    elif departInput == "EASTEREGG":surprise()
    elif departInput == "Q":exit()
    else:print("Veuillez entrer une lettre valide")

depart()
