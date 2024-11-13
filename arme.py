class Arme:
    def __init__(self, nom, degats):
        self.nom = nom
        self.degats = degats

    def __str__(self):
        return f"{self.nom} (Dégâts: {self.degats})"
