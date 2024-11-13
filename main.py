import json
from datetime import datetime
from joueur import Joueur
from monstre import Monstre
from arme import Arme

class Jeu:
    def __init__(self):
        self.grille = [['X' for _ in range(10)] for _ in range(6)]
        self.joueur_pos = (2, 1)  # Position initiale de P
        self.grille[self.joueur_pos[0]][self.joueur_pos[1]] = 'P'

    def afficher_grille(self):
        for ligne in self.grille:
            print(''.join(ligne))
        print("Déplacez P (haut, bas, gauche, droite) ou 'quitter' pour sortir:")

    def deplacer_joueur(self, direction):
        # Enlever P de la position actuelle
        self.grille[self.joueur_pos[0]][self.joueur_pos[1]] = 'X'

        if direction == 'haut' and self.joueur_pos[0] > 0:
            self.joueur_pos = (self.joueur_pos[0] - 1, self.joueur_pos[1])
        elif direction == 'bas' and self.joueur_pos[0] < len(self.grille) - 1:
            self.joueur_pos = (self.joueur_pos[0] + 1, self.joueur_pos[1])
        elif direction == 'gauche' and self.joueur_pos[1] > 0:
            self.joueur_pos = (self.joueur_pos[0], self.joueur_pos[1] - 1)
        elif direction == 'droite' and self.joueur_pos[1] < len(self.grille[0]) - 1:
            self.joueur_pos = (self.joueur_pos[0], self.joueur_pos[1] + 1)

        # Remettre P à sa nouvelle position
        self.grille[self.joueur_pos[0]][self.joueur_pos[1]] = 'P'

    def sauvegarder(self):
        # Obtenir la date actuelle pour le nom de fichier
        date_sauvegarde = datetime.now().strftime("%Y%m%d_%H%M%S")
        nom_fichier = f'sauvegarde_{date_sauvegarde}.json'
        
        with open(nom_fichier, 'w') as f:
            json.dump({
                'grille': self.grille,
                'joueur_pos': self.joueur_pos,
                'date_sauvegarde': date_sauvegarde,
            }, f)
        print(f"Jeu sauvegardé sous {nom_fichier}.")

    def charger(self):
        print("Aucune sauvegarde chargée au démarrage.")

    def jouer(self):
        self.charger()  # Charger la sauvegarde au démarrage (optionnel)
        while True:
            self.afficher_grille()
            commande = input()

            if commande == 'quitter':
                self.sauvegarder()  # Sauvegarder avant de quitter
                print("Jeu terminé.")
                break
            elif commande in ['haut', 'bas', 'gauche', 'droite']:
                self.deplacer_joueur(commande)
            else:
                print("Commande invalide. Essayez 'haut', 'bas', 'gauche', 'droite' ou 'quitter'.")

    def combat(self, joueur, monstre):
        print("--- Début du combat ---")
        while joueur.points_de_vie > 0 and monstre.points_de_vie > 0:
            joueur.attaquer(monstre)
            if monstre.points_de_vie > 0:
                monstre.attaquer(joueur)
        if joueur.points_de_vie > 0:
            print("Joueur a gagné le combat!")
        else:
            print("Monstre a gagné le combat!")

if __name__ == "__main__":
    # Lancer le jeu
    jeu = Jeu()
    jeu.jouer()

    # Initialisation du combat après la fin du jeu
    joueur = Joueur("Héros", 100)
    monstre = Monstre("Monstre", 50)

    # Création d'armes
    epee = Arme("Épée", 15)
    hache = Arme("Hache", 20)

    # Équiper l'arme au joueur
    joueur.equiper_arme(epee)

    # Commencer le combat
    jeu.combat(joueur, monstre)
