#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Excercice 6 : Echange de 2 valeurs
"""
#fichier: TP1_1.py
#auteur: Panthier Sharon
#date: septembre 2018

# --------------- imports --------------------------------

# -------------- Programme Principal --------------------
# Récupération des saisie utilisateur
var1 = input("Entrer la première saisie : ")
var2 = input("Entrez une deuxième saisie : ")

print("La valeur 1 : {} et la valeur 2 : {}".format(var1, var2))

# On échange les deux valeurs a l'aide d'une troisième qui stockera la première valeur
var3 = var1
var1=var2
var2=var3

# Affichage du résultat
print("La valeur 1 : {} tandis que la valeur 2 : {}".format(var1,var2))

"""
---- Résultats de l'exécution
Entrer la première saisie : Arbre
Entrez une deuxième saisie : Chaise
La valeur 1 : Arbre et la valeur 2 : Chaise
La valeur 1 : Chaise tandis que la valeur 2 : Arbre
>>>
Entrer la première saisie : 32
Entrez une deuxième saisie : 85
La valeur 1 : 32 et la valeur 2 : 85
La valeur 1 : 85 tandis que la valeur 2 : 32


"""
