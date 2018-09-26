#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Excercice 2 : Transtypage de saisies utilisateur
"""
#fichier: TP1_2.py
#auteur: Panthier Sharon
#date: septembre 2018

# --------------- imports --------------------------------

# -------------- Programme Principal --------------------
#Demande de saisie de l'utilisateur
var1 = input("Quelle est la première valeur ? ")
var2 = input("Quelle est la deuxième valeur ? ")

#Transtypage des valeurs en entiers
var1 = int(var1)
var2 = int(var2)

# Somme des deux valeur
var_somme = var1 + var2

# Affichage du résultat
print("La somme des deux valeurs est",var_somme)

"""
---- Résultats de l'exécution
Quelle est la première valeur ? 12
Quelle est la deuxième valeur ? 85
La somme des deux valeurs est 97
>>>
Quelle est la première valeur ? trois
Quelle est la deuxième valeur ? 3
Traceback (most recent call last):
  File "TP1_2.py", line 18, in <module>
    var1 = int(var1)
ValueError: invalid literal for int() with base 10: 'trois'
>>>
Quelle est la première valeur ? 2.3
Quelle est la deuxième valeur ? 1.0
Traceback (most recent call last):
  File "TP1_2.py", line 18, in <module>
    var1 = int(var1)
ValueError: invalid literal for int() with base 10: '2.3'

"""
