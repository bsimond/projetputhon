import repertoire_utils_text as repertoire_utils

## fonction rechercher par nom
def chercher_personnes(listerepertoire, nom):
    results = []
    for contact in listerepertoire:
        if nom in contact["nom"]:
            results.append(contact)
    return results


## fonction pour supprimer un contact
def supprimer_personne(repertoire, nom):
    for contact in repertoire:
        if nom == contact["nom"]:
            repertoire_utils.del_rep( repertoire, contact)
    if nom != contact ["nom"]:
            print("le contact n'existe pas")


## fonction pour ajouter un conatct
def ajouter_personne(listerepertoire, nouveaunom, nouveaunumero , nouveaumail):
    if chercher_personnes(listerepertoire, nouveaunom,):
         return False
    else:
        newcontact ={"nom": nouveaunom, "tel": nouveaunumero, "mail": nouveaumail}
        repertoire_utils.append_rep(listerepertoire, newcontact)
        return True


def get_rep():
    return repertoire_utils.get_rep()

def lister_tous_les_contact(repertoire):
    contacts = []
    for contact in repertoire:
        contacts.append (contact)
    return contacts


