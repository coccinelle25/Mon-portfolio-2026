nombres = [5, 8, 10]

t = nombres[0]
nombres[0] = nombres[2]
nombres[2] = t

print(nombres)

def rechercher_element(liste, element):
    for i in range(len(liste)):
        if liste[i] == element:
            return i
    return  None
    
def rechercher_element2(liste, element):
    taille = len(liste)
    if taille == 0:
        return None
    if liste[taille-1] == element:
        return taille -1
    
    return rechercher_element2(liste[:-1], element)

        
rep = rechercher_element(nombres, 8)
print(f"Indice de 8 dans {nombres} = {rep}")
rep = rechercher_element(nombres, 20)
print(f"Indice de 20 dans {nombres} = {rep}")
