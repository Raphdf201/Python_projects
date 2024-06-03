import math

resultat = 0.0


def addition(nb_1, nb_2):
    return nb_1 + nb_2


def soustraction(nb_1, nb_2, resultat):
    resultat = nb_1 - nb_2
    return resultat


def multiplication(nb_1, nb_2, resultat):
    resultat = nb_1 * nb_2
    return resultat


def division(nb_1, nb_2, resultat):
    resultat = nb_1 / nb_2
    return resultat


def puissance(nb_1, nb_2, resultat):
    resultat = nb_1 ** nb_2
    return resultat


def racine_carree(nb_1):
    resultat = math.sqrt(nb_1)
    return resultat


quoi = input("Quelle opération voulez-vous exécuter ? (+, -, *, /, ^, rc) : ")
if quoi == "+":
    nb_1 = float(input("Nombre 1 à Additionner : "))
    nb_2 = float(input("Nombre 2 à Additionner : "))
    addition(nb_1, nb_2)
    print("Le résultat est ", resultat)
elif quoi == "-":
    nb_1 = float(input("Nombre 1 à soustraire : "))
    nb_2 = float(input("Nombre 2 à soustraire : "))
    soustraction(nb_1, nb_2, resultat)
    print("Le résultat est ", resultat)
elif quoi == "*":
    nb_1 = float(input("Nombre 1 à multiplier : "))
    nb_2 = float(input("Nombre 2 à multiplier : "))
    multiplication(nb_1, nb_2, resultat)
    print("Le résultat est ", resultat)
elif quoi == "/":
    nb_1 = float(input("Nombre 1 à diviser : "))
    nb_2 = float(input("Nombre 2 à diviser : "))
    division(nb_1, nb_2, resultat)
    print("Le résultat est ", resultat)
elif quoi == "^":
    nb_1 = float(input("Nombre : "))
    nb_2 = int(input("Exposant : "))
    puissance(nb_1, nb_2, resultat)
    print("Le résultat est ", resultat)
elif quoi == "rc":
    nb_1 = int(input("Nombre : "))
    racine_carree(nb_1)
    print("Le résultat est ", resultat)
else:
    print("Veuillez entrer un symbole valide.")
    print("(+) = addition, (-) = soustraction, (*) = multiplication")
    print("(/) = division, (^) = exposant ou puissance, (rc) = racine carrée")

# Donne 0 à chaque opération (donc non fonctionnelle)
