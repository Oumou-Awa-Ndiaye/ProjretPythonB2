# monstre.py
from entite import Entite  # Import de la classe Entite

class Monstre(Entite):
    def __init__(self, nom, points_de_vie, force):
        super().__init__(nom, points_de_vie)
        self.force = force
    
    def attaquer(self, cible):
        print(f"{self.nom} attaque {cible.nom} et inflige {self.force} points de dégâts.")
        cible.recevoir_degats(self.force)
