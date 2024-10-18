# entite.py

class Entite:
    def __init__(self, nom, points_de_vie):
        self.nom = nom
        self.points_de_vie = points_de_vie
    
    def attaquer(self, cible):
        pass  # Méthode à redéfinir dans les sous-classes
    
    def recevoir_degats(self, degats):
        self.points_de_vie -= degats
        print(f"{self.nom} reçoit {degats} points de dégâts. Il lui reste {self.points_de_vie} points de vie.")
        
    def est_vivant(self):
        return self.points_de_vie > 0
