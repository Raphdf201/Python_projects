print("Ce programme transforme nimporte quel chiffre à 3 avec la formule suivante : (x*2+6)/2-x=3")
nbr_debut = int(input("Entrez votre nombre (x) : "))
nbr_milieu_debut = nbr_debut * 2
print(nbr_debut, "* 2 =", nbr_milieu_debut)
nbr_milieu_fin = nbr_milieu_debut + 6
print(nbr_milieu_debut, "+ 6 =", nbr_milieu_fin)
nbr_fin = nbr_milieu_fin / 2 - nbr_debut
print(nbr_milieu_fin, "/ 2 =", int(nbr_fin))
print("(", nbr_debut, "* 2 + 6 ) / 2 -", nbr_debut, "=", int(nbr_fin))