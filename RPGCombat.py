from PIL import Image, ImageTk  # Vous devez installer Pillow : pip install Pillow
import tkinter as tk
from tkinter import ttk, scrolledtext

class RPGCombatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Combat RPG")

        # Ajouter des images pour le héros et le dragon
        self.heros_img = ImageTk.PhotoImage(Image.open("heros.png").resize((100, 100)))
        self.dragon_img = ImageTk.PhotoImage(Image.open("dragon.png").resize((100, 100)))
        
        # Affichage des images
        self.heros_label = tk.Label(self.root, image=self.heros_img)
        self.heros_label.grid(row=0, column=0)
        self.dragon_label = tk.Label(self.root, image=self.dragon_img)
        self.dragon_label.grid(row=0, column=1)

        # Créer une zone de texte défilante pour les messages
        self.text_area = scrolledtext.ScrolledText(self.root, width=40, height=10)
        self.text_area.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Barre de santé du héros et du dragon
        self.heros_health = ttk.Progressbar(self.root, length=200, maximum=100)
        self.heros_health.grid(row=2, column=0, padx=10, pady=10)
        self.heros_health['value'] = 100
        self.dragon_health = ttk.Progressbar(self.root, length=200, maximum=120)
        self.dragon_health.grid(row=2, column=1, padx=10, pady=10)
        self.dragon_health['value'] = 120

        # Bouton pour commencer le combat
        self.combat_button = tk.Button(self.root, text="Commencer le Combat", command=self.commencer_combat)
        self.combat_button.grid(row=3, column=0, columnspan=2, pady=10)

    def commencer_combat(self):
        # La même logique de combat qu'avant
        pass

# Lancer l'application
root = tk.Tk()
app = RPGCombatApp(root)
root.mainloop()
