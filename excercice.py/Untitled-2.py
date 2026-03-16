etudiant = {"nom":"Vincent", 
            "age": 28, 
            "notes":[12,13.3,10]
            }
def calculer_moyenne(etud):
    somme = 0
    for note in etud["notes"]:
        somme += note
        return round(somme / len(etud["notes"]), 1)
    
    moyenne = calculer_moyenne(etudiant)
    print(f"Moyenne de {etudiant['nom']} vaut {moyenne}")