#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Excercice 1 : Récupération et affichage des saisies
"""
#fichier: TP1_1.py
#auteur: Panthier Sharon
#date: septembre 2018

# --------------- imports --------------------------------



# -------------- Programme Principal --------------------
# Récuprération des variables nom, prenom, age
nom=input("Quel est ton nom ? ")
prenom=input("Quel est ton prenom ? ")
age=input("Quel est ton age ? ")
age=int(age)
# Affectation des variables dans une phrase 
phrase="bonjour {1} {0}, tu as {2} ans.".format(nom,prenom,age)

# Afichage de la phrase
print(phrase)


"""
---- Résultats de l'exécution
Quel est ton nom ? Doe
Quel est ton prenom ? John
Quel est ton age ? 25
bonjour John Doe, tu as 25 ans.
>>>
Quel est ton nom ? Streisand
Quel est ton prenom ? Barbara
Quel est ton age ? dix-huit
Traceback (most recent call last):
  File "TP1_1.py", line 19, in <module>
    age=int(age)
ValueError: invalid literal for int() with base 10: 'dix-huit'

"""
