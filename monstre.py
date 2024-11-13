class Monstre:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, cible):
        degats = 10  # Dégâts de base
        cible.recevoir_degats(degats)
        print(f"{self.nom} attaque {cible.nom} et inflige {degats} points de dégâts.")

    def recevoir_degats(self, degats):
        self.vie -= degats
        print(f"{self.nom} reçoit {degats} points de dégâts. Il lui reste {self.vie} points de vie.")
