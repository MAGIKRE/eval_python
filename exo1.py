def trouver_groupes_somme_zero(liste):
    resultats = []
    n = len(liste)

    liste.sort()

    for i in range(n - 2):
        if i > 0 and liste[i] == liste[i - 1]:
            continue

        gauche = i + 1
        droite = n - 1

        while gauche < droite:
            somme = liste[i] + liste[gauche] + liste[droite]
            if somme == 0:
                resultats.append([liste[i], liste[gauche], liste[droite]])
                while gauche < droite and liste[gauche] == liste[gauche + 1]:
                    gauche += 1
                while gauche < droite and liste[droite] == liste[droite - 1]:
                    droite -= 1

                gauche += 1
                droite -= 1
            elif somme < 0:
                gauche += 1
            else:
                droite -= 1

    return resultats

ma_liste = [2 , 7 , 9 , -9]
groupes = trouver_groupes_somme_zero(ma_liste)
print("Groupes de 3 éléments dont la somme est égale à 0 :", groupes)
