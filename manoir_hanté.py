# Manoir hanté

from random import randint
print('Le manoir hanté.')
# Variables - def var = varname "=" varvalue
je_suis_courageux = True
score = 0
while je_suis_courageux:
    porte_fantome = randint(1, 3)
    print('Il y a trois portes devant toi,')
    print('Derrière une d entre elles se cache un fantôme.')
    print('Laquelle vas-tu ouvrir ?')
    porte = input('1, 2 ou 3 ? ')
    num_porte = int(porte)
    if num_porte == 0:
        print("Veuillez choisir un nombre entre 1 et 3")
        exit()
    elif num_porte > 3:
        print("Veuillez choisir un nombre entre 1 et 3")
        exit()
    if num_porte == porte_fantome:
        print('UN FANTÔME !!!')
        je_suis_courageux = False
    else:
        print('Ouf, pas de fantôme')
        print('Passons à la prochaine salle.')
        score = score + 1
print('AU SECOURS !!')
print('Partie terminée ! Ton score :', score)