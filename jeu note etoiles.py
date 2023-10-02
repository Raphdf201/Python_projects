"""
À faire :
1. adapter la variable personne dans les fonctions etoiles_1 à 5
"""
personne_1 = None
personne_2 = None
personne_3 = None
personne_4 = None
personne_5 = None
personne_6 = None
personne_7 = None
personne_8 = None
personne_9 = None
personne_10 = None


def attribuer_etoiles_1():
    print()


def attribuer_etoiles_2():
    print()


def attribuer_etoiles_3():
    print()


def attribuer_etoiles_4():
    print()


def attribuer_etoiles_5():
    print()


def voir_note():
    input_voir_note = input("De quelle personne voulez-vous voir la note ? (Personne 1 à 10) : ")
    personne = None
    if input_voir_note == "Personne 1":
        personne = personne_1
    elif input_voir_note == "Personne 2":
        personne = personne_2
    elif input_voir_note == "Personne 3":
        personne = personne_3
    elif input_voir_note == "Personne 4":
        personne = personne_4
    elif input_voir_note == "Personne 5":
        personne = personne_5
    elif input_voir_note == "Personne 6":
        personne = personne_6
    elif input_voir_note == "Personne 7":
        personne = personne_7
    elif input_voir_note == "Personne 8":
        personne = personne_8
    elif input_voir_note == "Personne 9":
        personne = personne_9
    elif input_voir_note == "Personne 10":
        personne = personne_10
    else:
        print("Veuillez entrer un nom valide.")

    if personne is not None:
        print(personne)


def combien_etoiles():
    input_combien_etoiles = input("Quelle note voulez-vous attribuer ? 1/2/3/4/5 étoile/s : ")
    if input_combien_etoiles == "1 étoile":
        etoiles_1()
    elif input_combien_etoiles == "2 étoiles":
        etoiles_2()
    elif input_combien_etoiles == "3 étoiles":
        etoiles_3()
    elif input_combien_etoiles == "4 étoiles":
        etoiles_4()
    elif input_combien_etoiles == "5 étoiles":
        etoiles_5()


def etoiles_1():
    input_personne_etoiles = input("À qui voulez-vous attribuer la note 1 étoile ? (Personne 1 à 10) : ")
    if input_personne_etoiles == "Personne_1":
        attribuer_etoiles_1()
    input_fin_etoile = input("Voulez-vous attribuer ou voir une autre note ? (oui/non) ")
    if input_fin_etoile == "oui":
        voir_attribuer()
    elif input_fin_etoile == "non":
        print("Bonne Journée !")
    else:
        print("Vous n'avez pas entré l'une des réponses attendues. Veuillez entrer «oui» ou «non».")
        combien_etoiles()


def etoiles_2():
    personne = input("À qui voulez-vous attribuer la note 2 étoiles ? ")
    input_fin_etoile = input("Voulez-vous attribuer ou voir une autre note ? (oui/non) ")
    if input_fin_etoile == "oui":
        voir_attribuer()
    elif input_fin_etoile == "non":
        print("Bonne Journée !")
    else:
        print("Vous n'avez pas entré l'une des réponses attendues. Veuillez entrer «oui» ou «non».")
        combien_etoiles()


def etoiles_3():
    personne = input("À qui voulez-vous attribuer la note 3 étoiles ? ")
    input_fin_etoile = input("Voulez-vous attribuer ou voir une autre note ? (oui/non) ")
    if input_fin_etoile == "oui":
        voir_attribuer()
    elif input_fin_etoile == "non":
        print("Bonne Journée !")
    else:
        print("Vous n'avez pas entré l'une des réponses attendues. Veuillez entrer «oui» ou «non».")
        combien_etoiles()


def etoiles_4():
    personne = input("À qui voulez-vous attribuer la note 4 étoiles ? ")
    input_fin_etoile = input("Voulez-vous attribuer ou voir une autre note ? (oui/non) ")
    if input_fin_etoile == "oui":
        voir_attribuer()
    elif input_fin_etoile == "non":
        print("Bonne Journée !")
    else:
        print("Vous n'avez pas entré l'une des réponses attendues. Veuillez entrer «oui» ou «non».")
        combien_etoiles()


def etoiles_5():
    personne = input("À qui voulez-vous attribuer la note 5 étoiles ? ")
    input_fin_etoile = input("Voulez-vous attribuer ou voir une autre note ? (oui/non) ")
    if input_fin_etoile == "oui":
        voir_attribuer()
    elif input_fin_etoile == "non":
        print("Bonne Journée !")
    else:
        print("Vous n'avez pas entré l'une des réponses attendues. Veuillez entrer «oui» ou «non».")
        combien_etoiles()


def voir_attribuer():
    input_voir_attribuer = input("Voulez-vous voir la note de quelqu'un ou attribuer une note à quelqu'un ? ("
                                 "attribuer note/voir note) ")
    if input_voir_attribuer == "attribuer note":
        combien_etoiles()
    elif input_voir_attribuer == "voir note":
        voir_note()
    else:
        print("Vous n'avez pas entré l'une des réponses attendues. Veuillez entrer «voir note» ou «attribuer note».")


voir_attribuer()
