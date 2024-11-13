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
        print(f"{self.nom} reçoit {degats} points de dégâts. Il lui reste {self.vie} points de vie.")

    def est_vivant(self):
        return self.vie > 0
