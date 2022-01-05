# -*- coding:Utf-8 -*-
# Programme developpe par ....
# date du ....
# Ceci est un programme presentant un menu en mode interactif/console


# ............................................................................................................
# Configuration de l'espace de travail...chargement des fonctionnalites utiles
# ............................................................................................................
# import os

# ............................................................................................................
# Definition des variables globales
# ............................................................................................................

# Variable representant la liste des menus
menuTitle = {"N": "> (N)ouvelle partie",
             "M": "> (M)anuel d'utilisation",
             "Q": "> (Q)uitter"}

# Variable globale indiquant vrai(True) si le programme doit continuer a s'executer
# et False dans le cas contraire
continuer_partie = True


# ............................................................................................................
# Definition des fonctions utilitaires
# ............................................................................................................
# print("\n" * 100) # un pseudo nettoyage de l'ecran..

def nettoyerEcran():
    """ Cette fonction nettoyer l'ecran du jeux ... """
    # os.system fonctionne uniquement si le programme est en mode console
    # res = os.system('cls' if os.name == 'nt' else 'clear')
    # if res:
    #    # res!=0 => la fonction ci-dessus ne s'est pas executee
    #    print("\n" * 100)
    print("\n" * 100)


def afficherMenu():
    """ cette fonction affiche le menu de l'application ... """
    print("Menu de l'application. Choississez l'option : ")
    for elt in menuTitle.values():
        print(elt)


def lancerNouvellePartie():
    """ Cette fonction relancer le jeux ... """
    global continuer_partie
    continuer_partie = True
    print("Une nouvelle partie de jeux va demarrer...")
    # Ici toutes les instuctions relative a une partie dujeux
    return 0  # indique que la fonction c'est acheve sans aucun soucis


def ouvrirManuelDuJeux():
    """Cette fonction affiche l'aide du manuel """
    print("Le jeux a été programme par Etudiant.\nPour y jouer, vous devez...")
    # sans return, ouvrirManuelDuJeux est une procedure..


def quitterJeux():
    """Cette fonction met un terme au jeux .... """
    global continuer_partie
    continuer_partie = False
    print("Le jeux prend fin.... Aurevoir joueur...")


def commandeInconnu():
    """ Cette fonction traite le cas des commandes qui n'ont pas ete prevu"""
    print("La commande saisie n'est pas reconnu... Tapez une des commandes du jeux\n")


# ............................................................................................................
# Le programme principale
# ............................................................................................................

menuAction = {"N": lancerNouvellePartie, "M": ouvrirManuelDuJeux, "Q": quitterJeux}
nettoyerEcran()

while continuer_partie:
    afficherMenu()
    choix = input()
    menuAction.get(choix, commandeInconnu)()
    # os.system("pause")
    input("\nTapez le bouton <Entre> pour poursuivre l'execution du programme ....")
    if choix.lower() != "q":
        nettoyerEcran()
