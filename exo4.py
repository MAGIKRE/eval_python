import re

def generer_listes(phrase):
    mots = re.findall(r'\w+\'?\w*', phrase)  
    separateurs = re.findall(r'[ ,]+', phrase)  

    if len(separateurs) < len(mots):
        separateurs.append(" ")  

    return [mots, separateurs]

phrase1 = "J'ai découvert Python cette semaine"
resultat1 = generer_listes(phrase1)
print("Résultat 1 :", resultat1)

