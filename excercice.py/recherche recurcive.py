etudiants = [
    {'mat' : '24FK572', 'nom' : 'FATUMA K. Laura'},
    {'mat' : '24KK114', 'nom' : 'KAPIMO K. Gaêl'},
    {'mat' : '24MK305', 'nom' : 'MWABWE K. Dimercia'},
    {'mat' : '24MK286', 'nom' : 'MULENGU K. Andy'},
    {'mat' : '24NW359', 'nom' : 'NGOY W. Pierre'},
    {'mat' : '24MM244', 'nom' : 'MBUZA M. Vincent'}
    ]

def rechercher_nom(liste_etudiants, matricule):
    """Retourne le nom de l'étudiant qui a ce matricule
    Retourne None si l'étudiant n'est pas trouvé"""

    for etu in liste_etudiants:
           if etu['mat'] == matricule:
               return etu ['nom']
    return None

matricule = input("Votre matricule: ")
print(rechercher_nom(etudiants, matricule))


import random
liste_nombres = [5,3,8,9,15,6]
def rechercher_indice_min(liste_nombres):
    """Retourne l'indice du plus petit de la liste"""
    taille = len(liste_nombres)
    i_min = 0

    for i in range (1, taille):
        if liste_nombres[i] < liste_nombres [i_min]:
            i_min = i

def generer_liste_alea(taille):
    liste =[]
    for i in range(taille):
        liste.append(random.randint(0, 50))
    return liste
def tri_selection(nombres):
    taille = len(nombres)
    for i in range(taille):
        i_min = 0

        for j in range(i + 1, taille):
            if nombres[j] < nombres[i_min]:
                i_min = j

        temp = nombres[i_min]
        nombres[i_min] = nombres[i]
        nombres[i] = temp

nombres = generer_liste_alea(10)
print(rechercher_indice_min(liste_nombres))

