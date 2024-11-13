class Joueur:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
        self.armes = []

    def equiper_arme(self, arme):
        self.armes.append(arme)

    def attaquer(self, cible):
        if self.armes:
            degats_total = sum(arme.degats for arme in self.armes)
            cible.recevoir_degats(degats_total)
            print(f"{self.nom} attaque {cible.nom} avec {' et '.join(str(arme) for arme in self.armes)}.")
        else:
            print(f"{self.nom} n'a pas d'arme pour attaquer.")

    def recevoir_degats(self, degats):
        self.vie -= degats
        print(f"{self.nom} reçoit {degats} points de dégâts. Il lui reste {self.vie} points de vie.")
