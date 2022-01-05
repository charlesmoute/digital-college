# -*- coding:Utf-8 -*-
# DigitalCollege Casino
# Description du projet : TP étudiants B1
# Date du projet :27/11/2020
# Auteur du projet : Charles Mouté

import math
from random import randrange

nom_casino = "<DigitalCollege Casino>"

# La variable continuer_programme est un booléen qui indique si notre programme est toujours en cours
# d'execution... il est vrai rant que l'on le programme doit continuer
continuer_programme = True

# Valeur minimal pour participer au DigitalCollege Casino
montant_minimal = 10000

# Numero de mise minimun
numero_min = 0
# Numero de mise maximin
numero_max = 49

while continuer_programme:

    # La variable continuer_jeux est un booleen qui indique si l'utilisateur souhaite jouer de nouveaux
    # apres la fin d'une mise donnée
    continuer_jeux = True

    # (1) Interface de saisie du montant de depart...
    print("\n[1] Interface de saisie du montant de depart")
    print("------------------------------------------------------------------------------\n")
    argent = 0  # montant depart avec lequel la roulette sera lancée
    while argent < montant_minimal:  # le montant minimale de la roulette est de 10000 fcfa
        argent = input("Entrez le montant de depart de : ")
        try:
            argent = int(argent)  # conversion en entier de la saisie de l'utilisateur
        except ValueError:
            # gestion de l'erreur d'execution éventuellement produite lors de la conversion de la saisie de
            # l'utilisateur
            print("La valeur ", argent, " n'est pas un nombre\n")
            argent = 0  # on reaffecte la valeur 0 pour que le programme se relance
            continue
        if montant_minimal > argent >= 0:
            # argent < montant_minimal and argent >= 0
            print("Votre montant de depart n'est pas suffisant pour jouer au", nom_casino, "\n",
                  "Il doit etre >= a ", montant_minimal, "\n")
        elif argent < 0:
            print("Le montant saisi est negatif\n")
        '''else:
            print("\n------------------------------------------------------------------------------\n")'''

    while continuer_jeux:
        # (2) Interface de saisie du numero de mise du joueur. Il doit etre compris entre 0 et 49, bornes incluses
        print("\n[2] Interface de saisie du numero de mise du joueur")
        print("------------------------------------------------------------------------------\n")
        numero_mise = numero_max + 1
        while numero_mise < numero_min or numero_mise > numero_max:
            numero_mise = input("\nEntrez le nombre sur lequel vous souhaitez miser vos gains : ")
            try:
                numero_mise = int(numero_mise)
            except ValueError:
                print("La valeur ", numero_mise, " n'est pas un nombre\n")
                numero_mise = numero_max + 1
                continue
            if numero_mise < numero_min:
                print("Le numero de mise est negatif\n")
            elif numero_mise > numero_max:
                print("Le numero de mise est superieur à 49\n")
            '''else:
                print("\n------------------------------------------------------------------------------\n")'''

        # (3) Montant mise par le joueur
        # Le joueur ne peut miser qu'un montant positif, inferieur ou egale a l'argent a sa disposition
        print("\n[3] Interface de montant de mise du joueur")
        print("------------------------------------------------------------------------------\n")
        montant_mise = 0
        while montant_mise <= 0 or montant_mise > argent:
            # pour autorise les emprunts le montant_mise peut être supérieur à agent
            # donc dans ce cas supprimer de la condition "or montant_mise > argent"
            montant_mise = input("Entrez le montant d'argent mise : ")
            try:
                montant_mise = int(montant_mise)
            except ValueError:
                print("La valeur ", montant_mise, " n'est pas un nombre\n")
                numero_mise = 0
                continue
            if montant_mise < 0:
                print("Le montant de mise est negatif\n")
            elif montant_mise == 0:
                print("Le montant de mise est nul\n")
            elif montant_mise > argent:
                print("Le montant de mise est superieur a votre stock\n".format(argent))
            '''else:
                print("\n------------------------------------------------------------------------------\n")'''

        # (4) Tirage aleatoire du numero gagnant par l'ordinateur
        numero_gagnant = randrange(0, 49)
        print("La roulette s'est arretee sur le numero gagnant suivant : ", numero_gagnant)

        # (5) Identification du resultat
        if numero_mise == numero_gagnant:
            argent += 3 * montant_mise
            print("Felicitations ! Vous avez gagne {0} FCFA".format(3 * montant_mise))
        elif (numero_mise % 2) == (numero_gagnant % 2):
            argent += math.ceil(montant_mise / 2)  # On procede a un arrondi au plus petit entier
            print("Felicitations vous avez mise sur la bonne couleur ! Vous remportez {0}".format(montant_mise / 2))
        else:
            print("Desolé vous avez perdu votre mise de ", montant_mise)
            argent -= montant_mise

        # (6) Test si le jeux peut continuer ou si on doit l'interrompre
        if argent > 0:
            print("Vos gains s'elevent à ", argent, "FCFA")
            reponse = input("Souhaitez-vous continuer avec le {0} ? (Oui/Non)\n".format(nom_casino))
            if reponse.lower().strip() == "non":  # conversion en minuscule avant de comparer...
                continuer_jeux = False
                continuer_programme = False
                print("Nous avons ete heureux de vous avoir comme joueur. Le programme va s'arreter....")
            else:
                print("Le jeux se poursuit ....")
        else:
            continuer_jeux = False
            if argent == 0:
                print("Vous n'avez plus d'argent")
                reponse = input("Souhaitez-vous quitter le {0} ? (Tapez 'Q' pour affirmatif)\n".format(nom_casino))
                if reponse.lower().strip() == "q":  # conversion en minuscule avant de comparer...
                    continuer_programme = False
                else:
                    print("Le jeux se poursuit ....")
            else:
                # ce code s'execute si et seulement si le gain du joueur est negatif.. ce qui n'est pas possible
                # dans cette version...pour le rendre possible dans la condition while de la section 2 il faudrait
                # supprimer de la condition l'instruction suivante "or montant_mise>argent".
                # Ainsi le code suivant ne s'executera que si et seulement si l'instruction ci-dessus est supprimé
                print("Vous n'avez plus d'argent et vous devez {0} au {1}".format(abs(argent), nom_casino))
                print("Le programme va s'arreter et vous serez poursuivi en justice...")
                continuer_programme = False
