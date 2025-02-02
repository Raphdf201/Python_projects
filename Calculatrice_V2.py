import math

result = 0.0


def add(nb_1, nb_2):
    return nb_1 + nb_2


def sub(nb_1, nb_2):
    return nb_1 - nb_2


def mult(nb_1, nb_2):
    return nb_1 * nb_2


def div(nb_1, nb_2):
    return nb_1 / nb_2


def exp(nb_1, nb_2):
    return nb_1 ** nb_2


def sqrt(nb_1):
    return math.sqrt(nb_1)


quoi = input("Quelle opération voulez-vous exécuter ? (+, -, *, /, ^, rc) : ")
if quoi == "+":
    nb_1 = float(input("Nombre 1 à Additionner : "))
    nb_2 = float(input("Nombre 2 à Additionner : "))
    result = add(nb_1, nb_2)
    print("Le résultat est ", result)
elif quoi == "-":
    nb_1 = float(input("Nombre 1 à soustraire : "))
    nb_2 = float(input("Nombre 2 à soustraire : "))
    result = sub(nb_1, nb_2)
    print("Le résultat est ", result)
elif quoi == "*":
    nb_1 = float(input("Nombre 1 à multiplier : "))
    nb_2 = float(input("Nombre 2 à multiplier : "))
    result = mult(nb_1, nb_2)
    print("Le résultat est ", result)
elif quoi == "/":
    nb_1 = float(input("Nombre 1 à diviser : "))
    nb_2 = float(input("Nombre 2 à diviser : "))
    result = div(nb_1, nb_2)
    print("Le résultat est ", result)
elif quoi == "^":
    nb_1 = float(input("Nombre : "))
    nb_2 = int(input("Exposant : "))
    result = exp(nb_1, nb_2)
    print("Le résultat est ", result)
elif quoi == "rc":
    nb_1 = int(input("Nombre : "))
    result = sqrt(nb_1)
    print("Le résultat est ", result)
else:
    print("Veuillez entrer un symbole valide.")
    print("(+) = addition, (-) = soustraction, (*) = multiplication")
    print("(/) = division, (^) = exposant ou puissance, (rc) = racine carrée")
