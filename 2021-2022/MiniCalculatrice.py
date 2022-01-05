# Programme d'une mini-calculatrice
# -*- coding:Utf-8 -*-

# Description du projet : Solution pour TP étudiants B1
# Date du projet :7/12/2020
# Auteur du projet : Charles Mouté

# ....................................................................................................................
# Chargement des modules utilitaires
# ....................................................................................................................
from tkinter import *

# ....................................................................................................................
# Definition des fonctions et variables utiles
# ....................................................................................................................
from tkinter import Label

couleur_ecrit = "white"
couleur_ecran = "#4E4E4E"
couleur_chiffre = "#797A79"
couleur_operateur = "#F1A23B"
couleur_autre = "#606060"

clicOperateur = False
miseAJour = False
resultat = ""
operateur = ""
MSG_ERREUR = "Pas un nombre"
ZERO = '0'


def fn_reinitialise():
    global clicOperateur
    global miseAJour
    global operateur
    global resultat

    if miseAJour or btn['C']['text'] == "AC":
        clicOperateur = False
        miseAJour = False
        operateur = ""
        resultat = ""
        ecran["text"] = ZERO
        btn['C']['text'] = "AC"
    if not miseAJour:
        clicOperateur = False
        ecran['text'] = ecran['text'][:-1]

        if len(ecran['text']) >= 2 and ecran['text'][-1] == ',':
            ecran['text'] = ecran['text'][:-1]

        if len(ecran['text']) >= 2 and ecran['text'] == '-0':
            ecran['text'] = ZERO

        btn['C']['text'] = "C"
        if len(ecran['text']) == 0 or ecran['text'] == ZERO:
            ecran["text"] = ZERO
            btn['C']['text'] = "AC"
            # miseAJour = True
            # fn_reinitialise()


def fn_chiffre0():
    global clicOperateur
    if miseAJour:
        fn_reinitialise()
    else:
        if clicOperateur:
            ecran["text"] = "0"
            clicOperateur = False
        elif ecran["text"] != ZERO:
            ecran["text"] += ZERO
        btn['C']['text'] = "C"


def fn_chiffre1():
    global clicOperateur
    if miseAJour:
        fn_reinitialise()
        ecran["text"] = "1"
    else:
        if clicOperateur:
            ecran["text"] = "1"
            clicOperateur = False
        else:
            if ecran["text"] == ZERO:
                ecran["text"] = "1"
            else:
                ecran["text"] += "1"
        btn['C']['text'] = "C"


def fn_chiffre2():
    global clicOperateur
    if miseAJour:
        fn_reinitialise()
        ecran["text"] = "2"
    else:
        if clicOperateur:
            ecran["text"] = "2"
            clicOperateur = False
        else:
            if ecran["text"] == ZERO:
                ecran["text"] = "2"
            else:
                ecran["text"] += "2"
        btn['C']['text'] = "C"


def fn_chiffre3():
    global clicOperateur
    if miseAJour:
        fn_reinitialise()
        ecran["text"] = "3"
    else:
        if clicOperateur:
            ecran["text"] = "3"
            clicOperateur = False
        else:
            if ecran["text"] == ZERO:
                ecran["text"] = "3"
            else:
                ecran["text"] += "3"
        btn['C']['text'] = "C"


def fn_chiffre4():
    global clicOperateur
    if miseAJour:
        fn_reinitialise()
        ecran["text"] = "4"
    else:
        if clicOperateur:
            ecran["text"] = "4"
            clicOperateur = False
        else:
            if ecran["text"] == ZERO:
                ecran["text"] = "4"
            else:
                ecran["text"] += "4"
        btn['C']['text'] = "C"


def fn_chiffre5():
    global clicOperateur
    if miseAJour:
        fn_reinitialise()
        ecran["text"] = "5"
    else:
        if clicOperateur:
            ecran["text"] = "5"
            clicOperateur = False
        else:
            if ecran["text"] == ZERO:
                ecran["text"] = "5"
            else:
                ecran["text"] += "5"
        btn['C']['text'] = "C"


def fn_chiffre6():
    global clicOperateur
    if miseAJour:
        fn_reinitialise()
        ecran["text"] = "6"
    else:
        if clicOperateur:
            ecran["text"] = "6"
            clicOperateur = False
        else:
            if ecran["text"] == ZERO:
                ecran["text"] = "6"
            else:
                ecran["text"] += "6"
        btn['C']['text'] = "C"


def fn_chiffre7():
    global clicOperateur
    if miseAJour:
        fn_reinitialise()
        ecran["text"] = "7"
    else:
        if clicOperateur:
            ecran["text"] = "7"
            clicOperateur = False
        else:
            if ecran["text"] == ZERO:
                ecran["text"] = "7"
            else:
                ecran["text"] += "7"
        btn['C']['text'] = "C"


def fn_chiffre8():
    global clicOperateur
    if miseAJour:
        fn_reinitialise()
        ecran["text"] = "8"
    else:
        if clicOperateur:
            ecran["text"] = "8"
            clicOperateur = False
        else:
            if ecran["text"] == ZERO:
                ecran["text"] = "8"
            else:
                ecran["text"] += "8"
        btn['C']['text'] = "C"


def fn_chiffre9():
    global clicOperateur

    if miseAJour:
        fn_reinitialise()
        ecran["text"] = "9"
    else:
        if clicOperateur:
            ecran["text"] = "9"
            clicOperateur = False
        else:
            if ecran["text"] == ZERO:
                ecran["text"] = "9"
            else:
                ecran["text"] += "9"
        btn['C']['text'] = "C"


def fn_decimal():
    if (not miseAJour) and (ecran["text"].find(",") == -1):
        ecran["text"] += ","


def fn_plusOuMoins():
    if (not miseAJour) and (ecran["text"] != ZERO):
        if ecran["text"].find("-") == -1:
            ecran["text"] = "-" + ecran["text"]
        else:
            ecran["text"] = ecran["text"][1:]


def fn_pourcentage():
    global resultat
    global clicOperateur
    global operateur
    if (not miseAJour) and (ecran["text"] != ZERO):
        operateur = ""
        clicOperateur = False
        resultat = float(ecran['text'].replace(',', '.'))/100
        ecran['text'] = str(resultat).replace('.', ',')


def fn_division():
    global resultat
    global operateur
    global clicOperateur

    if not miseAJour:
        clicOperateur = True
        operateur = '/'
        resultat = float(ecran["text"].replace(',', '.'))


def fn_multiplication():
    global resultat
    global operateur
    global clicOperateur

    if not miseAJour:
        clicOperateur = True
        operateur = '*'
        resultat = float(ecran["text"].replace(',', '.'))


def fn_soustraction():
    global resultat
    global operateur
    global clicOperateur

    if not miseAJour:
        clicOperateur = True
        operateur = '-'
        resultat = float(ecran["text"].replace(',', '.'))


def fn_addition():
    global resultat
    global operateur
    global clicOperateur

    if not miseAJour:
        clicOperateur = True
        operateur = '+'
        resultat = float(ecran["text"].replace(',', '.'))


def fn_calcul():
    global resultat
    global miseAJour
    global operateur

    if (not miseAJour) and operateur != "":

        if isinstance(resultat, str):
            resultat = float(ecran["text"].replace(',', '.'))

        if operateur == "/":
            if ecran['text'] == ZERO:
                ecran['text'] = MSG_ERREUR
                miseAJour = True
                resultat = ""
                operateur = ""
            else:
                resultat /= float(ecran['text'].replace(',', '.'))
                if (resultat % 1) == 0:
                    resultat = int(resultat)
                ecran['text'] = str(resultat).replace('.', ',')
        elif operateur == "*":
            resultat *= float(ecran['text'].replace(',', '.'))
            if (resultat % 1) == 0:
                resultat = int(resultat)
            ecran['text'] = str(resultat).replace('.', ',')
        elif operateur == "+":
            resultat += float(ecran['text'].replace(',', '.'))
            if (resultat % 1) == 0:
                resultat = int(resultat)
            ecran['text'] = str(resultat).replace('.', ',')
        elif operateur == "-":
            resultat -= float(ecran['text'].replace(',', '.'))
            if (resultat % 1) == 0:
                resultat = int(resultat)
            ecran['text'] = str(resultat).replace('.', ',')


btn_action = {"C": fn_reinitialise, "+/-": fn_plusOuMoins, "%": fn_pourcentage, "/": fn_division,
              "7": fn_chiffre7, "8": fn_chiffre8, "9": fn_chiffre9, "x": fn_multiplication,
              "4": fn_chiffre4, "5": fn_chiffre5, "6": fn_chiffre6, "-": fn_soustraction,
              "1": fn_chiffre1, "2": fn_chiffre2, "3": fn_chiffre3, "+": fn_addition,
              "0": fn_chiffre0, ",": fn_decimal, "=": fn_calcul}

btn_config = {"C": {"background": couleur_autre, "column": 0, "row": 1, "columnspan": 1},
              "+/-": {"background": couleur_autre, "column": 1, "row": 1, "columnspan": 1},
              "%": {"background": couleur_autre, "column": 2, "row": 1, "columnspan": 1},
              "/": {"background": couleur_operateur, "column": 3, "row": 1, "columnspan": 1},
              "7": {"background": couleur_chiffre, "column": 0, "row": 2, "columnspan": 1},
              "8": {"background": couleur_chiffre, "column": 1, "row": 2, "columnspan": 1},
              "9": {"background": couleur_chiffre, "column": 2, "row": 2, "columnspan": 1},
              "x": {"background": couleur_operateur, "column": 3, "row": 2, "columnspan": 1},
              "4": {"background": couleur_chiffre, "column": 0, "row": 3, "columnspan": 1},
              "5": {"background": couleur_chiffre, "column": 1, "row": 3, "columnspan": 1},
              "6": {"background": couleur_chiffre, "column": 2, "row": 3, "columnspan": 1},
              "-": {"background": couleur_operateur, "column": 3, "row": 3, "columnspan": 1},
              "1": {"background": couleur_chiffre, "column": 0, "row": 4, "columnspan": 1},
              "2": {"background": couleur_chiffre, "column": 1, "row": 4, "columnspan": 1},
              "3": {"background": couleur_chiffre, "column": 2, "row": 4, "columnspan": 1},
              "+": {"background": couleur_operateur, "column": 3, "row": 4, "columnspan": 1},
              "0": {"background": couleur_chiffre, "column": 0, "row": 5, "columnspan": 2},
              ",": {"background": couleur_autre, "column": 2, "row": 5, "columnspan": 1},
              "=": {"background": couleur_operateur, "column": 3, "row": 5, "columnspan": 1}}

# ....................................................................................................................
# Programme principal
# ....................................................................................................................
fenetre = Tk()
fenetre.title("Mini Calcultrice")
# fenetre.columnconfigure(0, weight=1)
# fenetre.rowconfigure(0, weight=1)
# fenetre.geometry("200x200")
fenetre.resizable(False, False)
# fenetre.configure(padx=0, pady=0, highlightthickness=0)
fenetre.configure(width=32, height=20)

# (1) Ecran d'affichage
# width=33, height=2,

ecran = Label(fenetre, text='0', font="Arial 25 bold", background=couleur_ecran, foreground="white", anchor=E,
              padx=10, width=32, height=3)
ecran.grid(column=0, row=0, columnspan=4, sticky=NSEW)

# Positionnement des boutons
btn = {}
for cle, valeur in btn_config.items():
    btn[cle] = Button(text=cle, highlightthickness=0,
                      # highlightbackground=btn_config[cle]["background"],
                      padx=5, pady=0, width=8, height=4,
                      relief=GROOVE, command=btn_action[cle])
    btn[cle].grid(column=btn_config[cle]["column"], row=btn_config[cle]["row"],
                  columnspan=btn_config[cle]["columnspan"], sticky=EW)
btn['C']['text'] = "AC"

# (4) Lancement de l'application
fenetre.mainloop()
