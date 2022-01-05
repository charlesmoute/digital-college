# Programme d'une ardoise dite magique
# -*- coding:Utf-8 -*-

# Description du projet : TP étudiants B1
# Date du projet :9/12/2020
# Auteur du projet : Charles Mouté

# ....................................................................................................................
# Chargement des modules utilitaires
# ....................................................................................................................
from tkinter import *

# ....................................................................................................................
# Variable utilitaire
# ....................................................................................................................
coord_x, coord_y = 0, 0


# ....................................................................................................................
# Definition des fonctions utilisateurs
# ....................................................................................................................
def effacerZone2Dessin():
    """ Action de nettoyage de l'ecran de dessin"""
    zone2Dessin.delete("all")


def sauvegarderPosition(event):
    """ Memorise la position du click de la souris"""
    global coord_x, coord_y
    coord_x, coord_y = event.x, event.y


def ajouterLigne(event):
    global coord_x, coord_y
    zone2Dessin.create_line((coord_x, coord_y, event.x, event.y), fill=couleurCrayon.get())
    coord_x, coord_y = event.x, event.y


def aPropos():
    """Fenêtre-message indiquant l'auteur et le type de licence"""
    msg = Toplevel(fenetre)
    Message(msg, width=400, aspect=100, justify=CENTER,
            text='Ardoise magique\n\n(C) DigitialCollege, Decembre 2020.\n\n' \
                 'Licence = GPL').pack(padx=10, pady=10)


def manuelUtilisation():
    """Fenêtre-message contenant la description sommaire du manuel d'utilisation de l'application"""
    msg = Toplevel(fenetre)
    Message(msg, bg="navy", fg="ivory", width=400, font="Helvetica 10 bold",
            text='Ceci est un manuel d\'utilisation .... \n' \
                 'Tout le monde devrait en ecrire un pour son application\n' \
                 'Juste pour le test !'
            ).pack(padx=10, pady=10)


# ....................................................................................................................
# Programme principal
# ....................................................................................................................
fenetre = Tk()
fenetre.title('Ardoise magique')
fenetre.columnconfigure(0, weight=1)
fenetre.rowconfigure(0, weight=1)
fenetre.resizable(False, False)

# (1) Menu de l'application
barre2Menu = Menu(fenetre)
fenetre.config(menu=barre2Menu)

# Ajout des elements de menu
# (1.1) Menu <Fichier>
menuFichier = Menu(barre2Menu)
barre2Menu.add_cascade(label="Fichier", menu=menuFichier)
menuFichier.add_command(label='Gommer', command=effacerZone2Dessin)
menuFichier.add_separator()
menuFichier.add_command(label="Quitter", command=fenetre.quit)

# (1.2) Menu <Aide>
menuAide = Menu(barre2Menu)
barre2Menu.add_cascade(label="Aide", menu=menuAide)
menuAide.add_command(label='Manuel d\'utilisation', command=manuelUtilisation)
menuAide.add_command(label='A propos ...', command=aPropos)

# ....................................................................................................................
# (1) Menu de l'application version 2
# barre2Menu = Frame()
# barre2Menu.grid(column=0, row=0, sticky=(N, W, E, S))

# (1.1) Menu <Fichier>
# menuFichier = Menubutton(barre2Menu, text='Fichier')
# menuFichier.pack(side=LEFT)
# eltMenu = Menu(menuFichier)
# eltMenu.add_command(label='Gommer', underline=0, command=effacerZone2Dessin)
# eltMenu.add_command(label='Quitter', underline=0, command=fenetre.quit)
# menuFichier.configure(menu=eltMenu)

# (1.2) Menu <Aide>
# menuAide = Menubutton(barre2Menu, text='Aide')
# menuAide.pack(side=LEFT)
# eltMenu = Menu(menuAide)
# eltMenu.add_command(label='Manuel d\'utilisation', underline=0, command=manuelUtilisation)
# eltMenu.add_command(label='A propos ...', underline=0, command=aPropos)
# menuAide.configure(menu=eltMenu)
# ....................................................................................................................

# (2) La zone de dessin
zone2Dessin = Canvas(fenetre, cursor='pencil', background="black")
zone2Dessin.grid(column=0, row=0, sticky=(N, W, E, S))
# zone2Dessin.grid(column=0, row=1, sticky=(N, W, E, S))
zone2Dessin.bind("<Button-1>", sauvegarderPosition)
zone2Dessin.bind("<B1-Motion>", ajouterLigne)

# (3) Le panneau des boutons
panneau2Boutons = Frame(fenetre)
panneau2Boutons.grid(column=0, row=1, sticky=(N, W, E, S))
# panneau2Boutons.grid(column=0, row=2, sticky=(N, W, E, S))

# (3.1) Boutons de selection des couleurs du crayon
couleurCrayon = StringVar()
# Valeur par defaut...
couleurCrayon.set("white")
btn_rouge = Radiobutton(panneau2Boutons, text='Rouge', variable=couleurCrayon, value='red')
btn_blanc = Radiobutton(panneau2Boutons, text='Blanc', variable=couleurCrayon, value='white')
btn_bleu = Radiobutton(panneau2Boutons, text='Bleu', variable=couleurCrayon, value='blue')

# Position des boutons sur le panneau des boutons
btn_blanc.grid(column=0, row=0)
btn_rouge.grid(column=1, row=0)
btn_bleu.grid(column=2, row=0)

# (3.2) Boutons pour nettoyer la zone de dessin
btn_effacer = Button(panneau2Boutons, text="Gomme", fg="green",
                     relief=GROOVE, highlightthickness=10, padx=5, pady=3,
                     command=effacerZone2Dessin)
btn_effacer.grid(column=3, row=0)

# (3.3) Boutons pour obtenir l'aide de l'application
# btn_manuel = Button(panneau2Boutons, text="Manuel", command=manuelUtilisation)
# btn_manuel.grid(column=4, row=0)

# (4) Lancement de l'application
fenetre.mainloop()
