from random import randint
print ('Ce dé peut générer des nombre aléatoires.')
print ('Veuillez entrer un par un les limites du dé (pour un dé à 6 faces, vous pourriez entrer 1 et 6)')
nb_1 = int(input("Entrez votre premier nombre (le plus petit) : "))
nb_2 = int(input("Entrez votre deuxième nombre (le plus grand) : "))
print ("Ce dé génèrera un nombre aléatoire entre", nb_1, "et", nb_2)
print ("Voici votre nombre : ", randint(nb_1, nb_2))
