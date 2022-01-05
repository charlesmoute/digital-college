# Programme de preparation du Riz
print("DigitalCollege : cuisson de preparation du riz")
reponseCorrect = False
temperature = 100
riz = 0
while not reponseCorrect:
    riz = input("> Quel est la quantite de riz que vous souhaitez cuire ?\n")
    try:
        riz = int(riz)
        assert 0 < riz <= 10
        reponseCorrect = True
    except ValueError:
        print("  La valeur saisie n'est pas un quantite")
    except AssertionError:
        print("  La quantite de riz doit etre un nombre strictement positif et <= a 10")
eau = 2*riz
sel = eau*0.5
print(f"> Versez dans la marmite {eau} verre(s) d'eau pour cuire {riz} verre(s) de riz")
print(f"> Ajoutez {sel} cuilleee de sel dans votre preparation")
print("> Mettre la marmite au feu et attendre l'ebullition de l'eau ...")
while temperature >= 0:
    print(f"({temperature}) L'eau est entrain de bouillir...")
    temperature -= 20
print("  L'eau a atteint la temperature d'ebullition...\nAjoutez le riz")
# On considere que le feu ou le temps de cuisson est fonction de la quantite d'eau
feu = 5*eau
while feu >= 0:
    print(f"  ({feu}) Le riz est entrain de cuire ...")
    feu -= 5
print("> Le riz est cuit...")
