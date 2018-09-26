#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Excercice 3 : Récupération et affichage des saisies
"""
#fichier: TP1_3.py
#auteur: Panthier Sharon
#date: septembre 2018

# --------------- imports --------------------------------

# -------------- Programme Principal --------------------
nombre1 = input("Entrez le premier nombre : ")
nombre1 = int(nombre1)
print("Valeur saisie :",nombre1)

nombre2 = input("Entrez le deuxième nombre : ")
nombre2 = int(nombre2)
print("Valeur saisie :",nombre2)

double_nombre2 = nombre2+nombre2
print("Le double du deuxième nombre :",double_nombre2)

if double_nombre2 == nombre1:
    print("{0} est bien le double de {1}".format(nombre1, nombre2))
else:
    print("{0} n'est pas le double de {1}".format(nombre1, nombre2))


"""
---- Résultats de l'exécution
Entrez le premier nombre : 10
Entrez le deuxième nombre : 5
Le nombre : 10 est bien le double de 5
>>>
Entrez le premier nombre : 8
Entrez le deuxième nombre : 11
Le nombre : 8 n'est pas le double de 11
>>>
Entrez le premier nombre : 15
Valeur saisie : 15
Entrez le deuxième nombre : 10
Valeur saisie : 10
Le double du deuxième nombre : 20
15 n'est pas le double de 10
>>>
Entrez le premier nombre : 40
Valeur saisie : 40
Entrez le deuxième nombre : 20
Valeur saisie : 20
Le double du deuxième nombre : 40
40 est bien le double de 20
"""
