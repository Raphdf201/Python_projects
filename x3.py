def x3():
    print("Ce programme transforme nimporte quel chiffre à 3 avec la formule suivante : (x*2+6)/2-x=3")
    x = int(input("Entrez votre nombre (x) : "))
    nbr_debut = x * 2
    nbr_milieu = nbr_debut + 6
    nbr_milieu_fin = nbr_milieu / 2
    nbr_fin = nbr_milieu_fin - x
    print(x, "* 2 =", nbr_debut)
    print(nbr_debut, "+ 6 =", nbr_milieu)
    print(nbr_milieu, "/ 2 =", int(nbr_milieu_fin))
    print(int(nbr_milieu_fin), "-", x, "=", int(nbr_fin))
    print("(", x, "* 2 + 6 ) / 2 -", x, "=", int(nbr_fin))