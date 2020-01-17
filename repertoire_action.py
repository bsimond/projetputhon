## fonction rechercher par nom
def rechercher_par_nom(listerepertoire, nom):
    results = []
    for contact in listerepertoire:
        if nom in contact["nom"]:
            results.append(contact)
    return results

## fonction pour supprimer un contact
def supprimer_contact(repertoire, nom):
    for contact in repertoire:
        if nom == contact["nom"]:
            repertoire.remove(contact)


## fonction pour ajouter un conatct
def ajouter_contact(listerepertoire, nouveau_element):
    if rechercher_par_nom(listerepertoire, nouveau_element):
         return False
    else:
        listerepertoire.append({"nom": nouveaunom, "tel": nouveaunumero, "mail": nouveaumail})
        return True

