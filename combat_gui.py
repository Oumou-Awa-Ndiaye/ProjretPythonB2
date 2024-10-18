import tkinter as tk
from tkinter import messagebox

class JeuRPG:
    def __init__(self, master):
        self.master = master
        self.master.title("Combat RPG")
        
        # Créer une zone d'affichage pour le texte
        self.text_area = tk.Text(self.master, height=15, width=50)
        self.text_area.pack(pady=10)
        
        # Créer un bouton pour commencer le combat
        self.bouton_combat = tk.Button(self.master, text="Commencer le Combat", command=self.combat)
        self.bouton_combat.pack()

    def combat(self):
        # Initialisation des paramètres du combat
        heros_vie = 50
        dragon_vie = 40
        epée_degats = 10
        dragon_degats = 8

        # Boucle de combat
        while heros_vie > 0 and dragon_vie > 0:
            self.text_area.insert(tk.END, "Héros attaque Dragon avec Épée légendaire\n")
            dragon_vie -= epée_degats
            if dragon_vie <= 0:
                self.text_area.insert(tk.END, f"Dragon reçoit {epée_degats} points de dégâts. Il lui reste 0 points de vie.\n")
                break
            else:
                self.text_area.insert(tk.END, f"Dragon reçoit {epée_degats} points de dégâts. Il lui reste {dragon_vie} points de vie.\n")

            self.text_area.insert(tk.END, f"Dragon attaque Héros et inflige {dragon_degats} points de dégâts.\n")
            heros_vie -= dragon_degats
            self.text_area.insert(tk.END, f"Héros reçoit {dragon_degats} points de dégâts. Il lui reste {heros_vie} points de vie.\n")
            self.text_area.insert(tk.END, "---\n")

        # Résultat du combat
        if heros_vie > 0:
            self.text_area.insert(tk.END, "Héros a gagné le combat!\n")
        else:
            self.text_area.insert(tk.END, "Dragon a gagné le combat!\n")

# Création de la fenêtre principale Tkinter
root = tk.Tk()
jeu = JeuRPG(root)
root.mainloop()
