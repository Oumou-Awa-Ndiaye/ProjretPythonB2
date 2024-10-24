# joueur.py
from entite import Entite  # Import de la classe Entite
from arme import Arme      # Import de la classe Arme


class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, autre):
        raise NotImplementedError("Cette méthode doit être implémentée dans les sous-classes")

    def recevoir_degats(self, degats):
        self.vie -= degats
        if self.vie < 0:
            self.vie = 0

    def est_vivant(self):
        return self.vie > 0


class Joueur(Personnage):
    def __init__(self, nom="Joueur", vie=50, arme="Épée"):
        super().__init__(nom, vie)
        self.arme = arme

    def attaquer(self, autre):
        degats = 12
        print(f"{self.nom} attaque {autre.nom} avec {self.arme}")
        autre.recevoir_degats(degats)
        print(f"{autre.nom} reçoit {degats} points de dégâts. Il lui reste {autre.vie} points de vie.")


class Monstre(Personnage):
    def __init__(self, nom="Monstre", vie=30):
        super().__init__(nom, vie)

    def attaquer(self, autre):
        degats = 10
        print(f"{self.nom} attaque {autre.nom} et inflige {degats} points de dégâts.")
        autre.recevoir_degats(degats)
        print(f"{autre.nom} reçoit {degats} points de dégâts. Il lui reste {autre.vie} points de vie.")


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

        # Avancer à l'attaquant suivant
        i = (i + 1) % len(liste_combat)

    # Résultat final
    print("---")
    if liste_combat[0].est_vivant():
        print(f"{liste_combat[0].nom} a gagné le combat!")


# Séquence de combat: DDDDDJDDD où D = Monstre, J = Joueur
sequence_combat = "DDDDDJDDD"

# Créer les personnages selon la séquence
liste_combat = creer_sequence_combat(sequence_combat)

# Lancer le combat
combat(liste_combat)
