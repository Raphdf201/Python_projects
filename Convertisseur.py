def longueur_cv():
    print("Convertisseur d'unités de mesure de longueur")


def energie_cv():
    print("Convertisseur d'unités de mesure d'énergie")


def vitesse_cv():
    print("Convertisseur d'unités de vitesse")


def surprise_cv():
    print("UWU")
    exit()


def launch_cv():
    print("Bienvenue dans mon convertisseur d'unités")
    departInput = input(
        "Pour convertir une unité de longueur, écrire L, pour l'énergie, E et Q pour quitter : ")
    if departInput == "L":
        longueur_cv()
    elif departInput == "E":
        energie_cv()
    elif departInput == "V":
        vitesse_cv()
    elif departInput == "EASTEREGG":
        surprise_cv()
    elif departInput == "Q":
        exit()
    else:
        print("Veuillez entrer une lettre valide")
