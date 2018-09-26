#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Excercice 4 : Division euclidienne
"""
#fichier: TP1_4.py
#auteur: Panthier Sharon
#date: septembre 2018

# --------------- imports --------------------------------

# -------------- Programme Principal --------------------

# Récupération des saisies faites par l'utilisateur
nombre1 = input("Entrez un entier positif : ")
nombre1 = int(nombre1)
print("Valeur saisie :",nombre1)

nombre2 = input("Entrez un deuxième entier positif : ")
nombre2 = int(nombre2)
print("Valeur saisie :",nombre2)

# Vérification que le deuxième nombre ne sois pas égale a 0
if nombre2 != 0:
    # calcul du quotient
    quotient = nombre1 / nombre2
    quotient =int(quotient)
    print("le quotien de la division est",quotient)
    
    # calcul du reste
    reste = nombre1 % nombre2
    print("le reste de la division est", reste)
    
    # affichage du résultat
    print("Division euclidienne: {0} = {1}*{2} +{3}".format(nombre1,nombre2, quotient, reste))
else:
    print("Erreur : une division ne peut etre faite sur un nombre null ( égal a 0)")

"""
---- Résultats de l'exécution
Entrez un entier positif : 78
Valeur saisie : 78
Entrez un deuxième entier positif : 6
Valeur saisie : 6
le quotien de la division est 13
le reste de la division est 0
Division euclidienne: 78 = 6*13 +0
>>>
Entrez un entier positif : 45
Valeur saisie : 45
Entrez un deuxième entier positif : 0
Valeur saisie : 0
Erreur : une division ne peut etre faite sur un nombre null ( égal a 0)
>>>
Entrez un entier positif : 11
Valeur saisie : 11
Entrez un deuxième entier positif : 25
Valeur saisie : 25
le quotien de la division est 0
le reste de la division est 11
Division euclidienne: 11 = 25*0 +11
"""
