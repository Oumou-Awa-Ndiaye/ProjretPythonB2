# joueur.py
from entite import Entite  # Import de la classe Entite
from arme import Arme      # Import de la classe Arme

class Joueur(Entite):
    def __init__(self, nom, points_de_vie, arme):
        super().__init__(nom, points_de_vie)
        self.arme = arme  # Un objet de type Arme
    
    def attaquer(self, cible):
        print(f"{self.nom} attaque {cible.nom} avec {self.arme.nom}")
        cible.recevoir_degats(self.arme.degats)
