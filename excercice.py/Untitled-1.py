def max_liste(liste):
    max_nb = liste[0]
    for nb in liste:
        if nb > max_nb:
            max_nb = nb
            return max_nb
nombres = [3,9,7,5]
maximum = max_liste(nombres)
print(f"Le max de {nombres} vaut {maximum}")



def aire_rectangle(longueur,largeur):

    return longueur * largeur
print(aire_rectangle (52,25))


def additionner(a,b):
   
    print(additionner(5,9))

    
""" 11. la fonction n'affichera rien
"""

"""def addition(a, b):  manque de deux points
    return a + b
print(addition(32,40)) manque de print pour afficher le resultat
"""


def est_pair(n):
    n = int(input("entrez un nombre:"))
    if n %2 :
        return True
    else:
        return False
print(
    
