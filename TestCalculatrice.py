# Calculatrice minimaliste
from tkinter import *

nb_click = 0


# définition de l'action à effectuer si l'utilisateur actionne
# la touche "enter" alors qu'il édite le champ d'entrée :
def evaluer(event):
    # Affichage des informations associer a l'evenement
    print(event)
    resultat.configure(text="Résultat = " + str(eval(entree.get())))


def compteClick():
    global nb_click
    nb_click += 1
    ecran["text"] = "Vous avez cliqué {} fois.".format(nb_click)


# ----- Programme principal : -----

# Creation de la fenetre principale du programme
fenetre = Tk()

# Configuration de notre interface
entree = Entry(fenetre)
entree.bind("<Return>", evaluer)
resultat = Label(fenetre)
ecran = Label(fenetre)

btn_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
btn_click = Button(fenetre, text="Count", command=compteClick)


# Affichage en ligne des composantes de l'interface
# entree.pack()
# resultat.pack()
# btn_click.pack()
# ecran.pack()
# btn_quitter.pack()

# Correction de l'interface
entree.grid(row=1, column=1)
resultat.grid(row=1, column=2)
btn_click.grid(row=2, column=1, sticky=W)
ecran.grid(row=2, column=2, sticky=W)
btn_quitter.grid(row=3, column=2)

# démarrage du gestionnaire d’événement
fenetre.mainloop()

# fermeture de la fenetre
fenetre.destroy()

# btn01 = Button(text="1", bg="blue", font="bold", width=8, height=4, relief=FLAT)#width=8, height=4
# btn01.grid(column=0, row=1, sticky=EW)
# btn02 = Button(text="2", background=couleur_operateur, foreground=couleur_ecrit,
#               highlightthickness=0, padx=0, pady=0, width=8, height=4, relief=FLAT)
# btn02.grid(column=1, row=1, sticky=EW)
# btn02.grid(row=2, column=0, columnspan=2, sticky=NSEW)
# btn03 = Button(text="3", background=couleur_operateur, highlightthickness=0, padx=0, pady=0, width=8, height=4, relief=FLAT)
# btn03.grid(column=2, row=1, sticky=EW)
# btn04 = Button(text="4", background=couleur_operateur, highlightthickness=0, padx=0, pady=0, width=8, height=4, relief=FLAT)
# btn04.grid(column=3, row=1, sticky=EW)