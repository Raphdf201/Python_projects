import math

def addition(nb_1, nb_2):
    resultat = None
    resultat = nb_1 + nb_2
    return resultat

def quelle_operation(q_o_input):
    if q_o_input == "+":
        nb_1 = input("Premier nombre à additionner : ")
        nb_2 = input("Deuxième nombre à additionner : ")
        addition(nb_1, nb_2)
        print()