def addition_listes(n1, n2):
    i, j = len(n1) - 1, len(n2) - 1
    retenue = 0
    resultat = []

    while i >= 0 or j >= 0 or retenue:

        chiffre_n1 = n1[i] if i >= 0 else 0
        chiffre_n2 = n2[j] if j >= 0 else 0

        somme = chiffre_n1 + chiffre_n2 + retenue

        resultat.append(somme % 10)

        retenue = somme // 10

        i -= 1
        j -= 1

    return resultat[::-1]

n1 = [8, 4, 0]
n2 = [8, 3]
total = addition_listes(n1, n2)
print("Total :", total)  # retourne [9, 2, 3]
