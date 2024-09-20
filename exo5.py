def deviner_nombre():
    print("Mémorisez un nombre entier entre 1 et 100, le script va essayer de le retrouver, ne trichez pas !")
    
    borne_min = 1
    borne_max = 100
    essais = 0
    derniere_proposition = None
    derniere_reponse = None
    triche_detectee = False

    while borne_min <= borne_max:
        proposition = (borne_min + borne_max) // 2
        essais += 1
        print(f"script propose {proposition}... +, - ou G ?")
        reponse = input().strip()

        if derniere_proposition is not None:
            if reponse == "-" and derniere_reponse == "+" and proposition <= derniere_proposition:
                print(f"Tricheur !!! A la réponse {essais-1} il avait été proposé {derniere_proposition} "
                      f"et répondu '+'. En proposant {proposition}, la réponse ne peut pas être '-'.")
                triche_detectee = True
                break
            if reponse == "+" and derniere_reponse == "-" and proposition >= derniere_proposition:
                print(f"Tricheur !!! A la réponse {essais-1} il avait été proposé {derniere_proposition} "
                      f"et répondu '-'. En proposant {proposition}, la réponse ne peut pas être '+'.")
                triche_detectee = True
                break

        derniere_proposition = proposition
        derniere_reponse = reponse

        if reponse == "+":
            borne_min = proposition + 1
        elif reponse == "-":
            borne_max = proposition - 1
        elif reponse == "G":
            print(f"script a trouvé {proposition} en {essais} coups !!!")
            return
        else:
            print("Réponse invalide. Veuillez répondre par +, - ou G.")

    if triche_detectee:
        print(f"J'ai gagné par forfait en {essais} coups !!!")
    else:
        print(f"Le script n'a pas pu trouver le nombre après {essais} essais. Assurez-vous de ne pas tricher !")

deviner_nombre()
