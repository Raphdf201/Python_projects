import random
import string

def generer_mot_de_passe(longueur, utilise_speciaux=False):
    caracteres = string.ascii_letters + string.digits
    if utilise_speciaux:
        caracteres += string.punctuation

    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

print("Générateur de mots de passe sécurisés")
longueur = int(input("Longueur du mot de passe : "))
utilise_speciaux = input("Utiliser des caractères spéciaux ? (oui/non) : ").lower() == "oui"
mot_de_passe = generer_mot_de_passe(longueur, utilise_speciaux)
print("Mot de passe généré :", mot_de_passe)
