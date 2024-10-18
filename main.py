# main.py

# Importation des classes depuis les fichiers séparés
from joueur import Joueur
from monstre import Monstre
from arme import Arme

def combat(joueur, monstre):
    while joueur.est_vivant() and monstre.est_vivant():
        joueur.attaquer(monstre)
        if monstre.est_vivant():
            monstre.attaquer(joueur)
        print("---")
    
    if joueur.est_vivant():
        print(f"{joueur.nom} a gagné le combat!")
    else:
        print(f"{monstre.nom} a gagné le combat!")

if __name__ == "__main__":
    # Créer une instance de Joueur et Monstre
    epee = Arme("Épée légendaire", 10)
    joueur1 = Joueur("Héros", 50, epee)
    monstre1 = Monstre("Dragon", 40, 8)

    # Lancer un combat
    combat(joueur1, monstre1)
