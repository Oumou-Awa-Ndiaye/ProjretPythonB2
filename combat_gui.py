# import tkinter as tk
# from tkinter import messagebox

# class JeuRPG:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Combat RPG")
        
#         # Créer une zone d'affichage pour le texte
#         self.text_area = tk.Text(self.master, height=15, width=50)
#         self.text_area.pack(pady=10)
        
#         # Créer un bouton pour commencer le combat
#         self.bouton_combat = tk.Button(self.master, text="Commencer le Combat", command=self.combat)
#         self.bouton_combat.pack()

#     def combat(self):
#         # Initialisation des paramètres du combat
#         heros_vie = 50
#         dragon_vie = 40
#         epée_degats = 10
#         dragon_degats = 8

#         # Boucle de combat
#         while heros_vie > 0 and dragon_vie > 0:
#             self.text_area.insert(tk.END, "Héros attaque Dragon avec Épée légendaire\n")
#             dragon_vie -= epée_degats
#             if dragon_vie <= 0:
#                 self.text_area.insert(tk.END, f"Dragon reçoit {epée_degats} points de dégâts. Il lui reste 0 points de vie.\n")
#                 break
#             else:
#                 self.text_area.insert(tk.END, f"Dragon reçoit {epée_degats} points de dégâts. Il lui reste {dragon_vie} points de vie.\n")

#             self.text_area.insert(tk.END, f"Dragon attaque Héros et inflige {dragon_degats} points de dégâts.\n")
#             heros_vie -= dragon_degats
#             self.text_area.insert(tk.END, f"Héros reçoit {dragon_degats} points de dégâts. Il lui reste {heros_vie} points de vie.\n")
#             self.text_area.insert(tk.END, "---\n")

#         # Résultat du combat
#         if heros_vie > 0:
#             self.text_area.insert(tk.END, "Héros a gagné le combat!\n")
#         else:
#             self.text_area.insert(tk.END, "Dragon a gagné le combat!\n")

# # Création de la fenêtre principale Tkinter
# root = tk.Tk()
# jeu = JeuRPG(root)
# root.mainloop()



class RPGCombatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Combat RPG")

        # Créer une zone de texte défilante
        self.text_area = scrolledtext.ScrolledText(self.root, width=40, height=10)
        self.text_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Barre de santé du héros
        self.heros_health_label = tk.Label(self.root, text="Santé Héros")
        self.heros_health_label.grid(row=1, column=0)
        self.heros_health = ttk.Progressbar(self.root, length=200, maximum=100)
        self.heros_health.grid(row=2, column=0, padx=10, pady=10)
        self.heros_health['value'] = 100

        # Barre de santé du dragon
        self.dragon_health_label = tk.Label(self.root, text="Santé Dragon")
        self.dragon_health_label.grid(row=1, column=1)
        self.dragon_health = ttk.Progressbar(self.root, length=200, maximum=120)
        self.dragon_health.grid(row=2, column=1, padx=10, pady=10)
        self.dragon_health['value'] = 120

        # Bouton pour commencer le combat
        self.combat_button = tk.Button(self.root, text="Commencer le Combat", command=self.commencer_combat)
        self.combat_button.grid(row=3, column=0, columnspan=2, pady=10)

    def commencer_combat(self):
        heros_vie = 100
        dragon_vie = 120
        epee_degats = 10
        dragon_degats = 15

        while heros_vie > 0 and dragon_vie > 0:
            # Héros attaque
            dragon_vie -= epee_degats
            self.text_area.insert(tk.END, f"Héros attaque et inflige {epee_degats} points de dégâts au Dragon.\n")
            self.dragon_health['value'] = dragon_vie
            self.root.update_idletasks()
            if dragon_vie <= 0:
                self.text_area.insert(tk.END, "Dragon est vaincu !\n")
                break

            # Dragon attaque
            heros_vie -= dragon_degats
            self.text_area.insert(tk.END, f"Dragon attaque et inflige {dragon_degats} points de dégâts au Héros.\n")
            self.heros_health['value'] = heros_vie
            self.root.update_idletasks()
            if heros_vie <= 0:
                self.text_area.insert(tk.END, "Le Héros est vaincu...\n")
                break

        # Forcer le défilement automatique vers le bas
        self.text_area.yview(tk.END)

