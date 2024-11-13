import os
import time

def afficher_grille(grille):
    os.system('cls' if os.name == 'nt' else 'clear')
    for ligne in grille:
        print("".join(ligne))

def deplacer_P():
    # Dimensions de la grille
    largeur = 10
    hauteur = 5

    # Créer une grille vide
    grille = [['X' for _ in range(largeur)] for _ in range(hauteur)]
    
    # Position initiale de P
    pos_P = [hauteur // 2, 0]  # [ligne, colonne]

    # Boucle pour déplacer P
    while True:
        # Réinitialiser la grille
        grille = [['X' for _ in range(largeur)] for _ in range(hauteur)]
        
        # Placer P dans la position actuelle
        grille[pos_P[0]][pos_P[1]] = 'P'  
        
        # Afficher la grille
        afficher_grille(grille)

        # Demander à l'utilisateur la direction
        direction = input("Déplacez P (haut, bas, gauche, droite) ou 'quitter' pour sortir: ").strip().lower()

        if direction == 'quitter':
            break
        elif direction == 'haut' and pos_P[0] > 0:
            pos_P[0] -= 1
        elif direction == 'bas' and pos_P[0] < hauteur - 1:
            pos_P[0] += 1
        elif direction == 'gauche' and pos_P[1] > 0:
            pos_P[1] -= 1
        elif direction == 'droite' and pos_P[1] < largeur - 1:
            pos_P[1] += 1
        else:
            print("Mouvement invalide, essayez encore.")
        
        # Pause pour voir le mouvement
        time.sleep(0.5)

    print("Jeu terminé.")
