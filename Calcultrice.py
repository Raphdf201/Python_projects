import math


def addition():
    print("Quels nombres voulez-vous additionner ?")
    addition_nb_1 = float(input("Nombre 1 : "))
    addition_nb_2 = float(input("Nombre 2 : "))
    resultat_addition = addition_nb_1 + addition_nb_2
    print(addition_nb_1, "+", addition_nb_2, "=", resultat_addition)


def soustraction():
    print("Quels nombres voulez-vous soustraire ?")
    soustraction_nb_1 = float(input("Nombre 1 : "))
    soustraction_nb_2 = float(input("Nombre 2 : "))
    resultat_soustraction = soustraction_nb_1 - soustraction_nb_2
    print(soustraction_nb_1, "-", soustraction_nb_2, "=", resultat_soustraction)


def multiplication():
    print("Quels nombres voulez-vous multiplier ?")
    multiplication_nb_1 = float(input("Nombre 1 : "))
    multiplication_nb_2 = float(input("Nombre 2 : "))
    resultat_multiplication = multiplication_nb_1 * multiplication_nb_2
    print(multiplication_nb_1, "*", multiplication_nb_2, "=", resultat_multiplication)


def division():
    print("Quels nombres voulez-vous diviser ?")
    division_nb_1 = float(input("Nombre 1 : "))
    division_nb_2 = float(input("Nombre 2 : "))
    resultat_division = division_nb_1 / division_nb_2
    print(division_nb_1, "÷", division_nb_2, "=", resultat_division)


def exposant():
    print("Quel nombre voulez-vous élever à la puissance ?")
    exposant_base = float(input("Base : "))
    exposant_exposant = int(input("Exposant : "))
    resultat_exposant = exposant_base ** exposant_exposant
    print(exposant_base, "^", exposant_exposant, "=", resultat_exposant)


def racine_carree():
    print("Quel nombre voulez-vous raciner ?")
    racine_nb = float(input("Nombre à raciner : "))
    resultat_racine = math.sqrt(racine_nb)
    print(racine_nb, "√ =", resultat_racine)


def pi():
    print("Pi =", math.pi)


def arrondir():
    input_arrondir = input("Voulez vous arrondir vers le haut à l'entier le plus haut ou le plus bas ? (haut ou bas) : "
                           )
    if input_arrondir == "haut":
        arrondir_haut_nb = float(input("Nombre à arrondir : "))
        resultat_arrondir_haut = math.ceil(arrondir_haut_nb)
        print(arrondir_haut_nb, "≃", resultat_arrondir_haut)
    elif input_arrondir == "bas":
        arrondir_bas_nb = float(input("Nombre à arrondir : "))
        resultat_arrondir_bas = math.floor(arrondir_bas_nb)
        print(arrondir_bas_nb, "≃", resultat_arrondir_bas)
    else:
        print("Vous n'avez pas entré l'une des réponses attendues. Veuillez entrer «haut» ou «bas».")


def quelle_autre_operation():
    input_quelle_autre_operation = input("Quelle opération voulez-vous effectuer ? (exposant, racine carrée, "
                                         "afficher pi ou arrondir) : ")
    if input_quelle_autre_operation == "exposant":
        exposant()
    elif input_quelle_autre_operation == "racine carrée":
        racine_carree()
    elif input_quelle_autre_operation == "afficher pi":
        pi()
    elif input_quelle_autre_operation == "arrondir":
        arrondir()
    else:
        print("Vous n'avez pas entré l'une des réponses attendues. Veuillez entrer «addition», «soustraction», "
              "«multiplication», «division» ou «autre».")


def quelle_operation():
    input_quelle_operation = input("Quelle opération voulez-vous effectuer ? (addition, soustraction, multiplication, "
                                   "division ou autre) : ")
    if input_quelle_operation == "addition":
        addition()
    elif input_quelle_operation == "soustraction":
        soustraction()
    elif input_quelle_operation == "multiplication":
        multiplication()
    elif input_quelle_operation == "division":
        division()
    elif input_quelle_operation == "autre":
        quelle_autre_operation()
    else:
        print("Vous n'avez pas entré l'une des réponses attendues. Veuillez entrer «addition», «soustraction», "
              "«multiplication», «division» ou «autre».")


print("Ceci est une calculatrice")
quelle_operation()
