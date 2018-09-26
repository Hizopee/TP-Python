#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Excercice 5 : équation du secon degré
"""
#fichier: TP1_5.py
#auteur: Panthier Sharon
#date: septembre 2018

# --------------- imports --------------------------------
from math import sqrt
# -------------- Programme Principal --------------------
def Afficher_equation(a,b,c):
    """ Display the user equation
    Keyword Arguments:
    a -- first coefficient
    b -- second coefficient
    c -- third coefficient
    """
    equation="L'équation saisie est donc %s^2" % a

    if b > 0:
        equation += " + " + str(b)
    else:
        equation += " " + str(b)
    equation +="x"
    if c > 0:
        equation += " + " + str(c)
    else:
        equation += " " + str(c)

    return equation   

# Récupération des saisies de l'utilisateur
a = input("Entrez le 1er coefficient du trinome : ")
a = float(a)

b = input("Entrez le 2eme coefficient du trinome : ")
b = float(b)

c = input("Entrez le 3eme coefficient du trinome : ")
c = float(c)

print("L'équation saisie est donc", Afficher_equation(a,b,c))

# Vérification que le premier coefficient n'est pas négatif
if a != 0:
    delta = b**2 - (4 * a * c)
    print("delta :", delta)
else:
    print("le premier coefficient ne doit pas etre négatif")
    
# Calcul des racines en fonction du delta
if delta < 0:
    print("L'équation n'a pas de racines réelles")
elif delta == 0:
    x=-(b/2*a)
    print("La racine double de l'équation est", x)
else:
    x1 = (-b -sqrt(delta)) / 2*a
    x1 = int(x1)
    
    x2 = (-b +sqrt(delta)) / 2*a
    x2 = int(x2)
    print("l'équation a deux racines dans R qui sont {0} et {1}".format(x1,x2))

""" 
---- Résultats de l'exécution
Entrez le 1er coefficient du trinome : 1
Entrez le 2eme coefficient du trinome : 2
Entrez le 3eme coefficient du trinome : -3
L'équation saisie est donc 1.0x^2 + 2.0x + -3.0
delta : 16.0
l'équation a deux racines dans R qui sont -3 et 1
>>>
Entrez le 1er coefficient du trinome : 4
Entrez le 2eme coefficient du trinome : 2
Entrez le 3eme coefficient du trinome : 1
L'équation saisie est donc 4.0x^2+2.0x+1.0
delta : -12.0
L'équation n'a pas de racines réelles

"""
