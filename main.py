# main.py

from personnages import Joueur, Monstre

def creer_sequence_combat(sequence):
    liste_combat = []
    for char in sequence:
        if char == 'J':
            liste_combat.append(Joueur())
        elif char == 'D':
            liste_combat.append(Monstre())
    return liste_combat


def combat(liste_combat):
    i = 0
    while len(liste_combat) > 1:
        print(f"--- Tour {i+1} ---")
        attaquant = liste_combat[i]
        defenseur = liste_combat[(i + 1) % len(liste_combat)]

        if attaquant.est_vivant() and defenseur.est_vivant():
            attaquant.attaquer(defenseur)

        if not defenseur.est_vivant():
            print(f"{defenseur.nom} est mort!")
            liste_combat.remove(defenseur)

        i = (i + 1) % len(liste_combat)

    print("---")
    if liste_combat[0].est_vivant():
        print(f"{liste_combat[0].nom} a gagné le combat!")


# Séquence de combat: DDDDDJDDD
sequence_combat = "DDDDDJDDD"

# Créer les personnages selon la séquence
liste_combat = creer_sequence_combat(sequence_combat)

# Lancer le combat
combat(liste_combat)
