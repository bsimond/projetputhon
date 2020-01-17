listerepertoire = [{"nom": "brice", "tel": "88555666", "mail": "brice@gmail.com"},
                   {"nom": "marion", "tel": "4557682", "mail": "marion@gmail.com"},
                   {"nom": "marcin", "tel": "454545", "mail": " marcin@gmail.Com"}]


## fonction pour afficher la liste
def liste_repertoire(listerepertoire):
    for ligne in listerepertoire:
        print(ligne["nom"], ligne["tel"], ligne["mail"])


## fonction rechercher par nom
def rechercher_par_nom(listerepertoire, nom):
    results = []
    for contact in listerepertoire:
        if nom in contact["nom"]:
            results.append(contact)
    return results


## fonction pour ajouter un conatct
def ajouter_contact(listerepertoire, nouveaunom, nouveaunumero, nouveaumal):
    if rechercher_par_nom(listerepertoire, nouveaunom):
        print("contact deja existant")
    else:
        listerepertoire.append({"nom": nouveaunom, "tel": nouveaunumero, "mail": nouveaumail})


## fonction pour supprimer un contact
def supprimer_conatct(repertoire, nom):
    for contact in repertoire:
        if nom == contact["nom"]:
            repertoire.remove(contact)
    # listerepertoire.remove ()


## liste des choix utilisateur
print(" L pour lister, ")
print(" A pour ajouter ")
print(" S pour supprimer")
print(" R pour recherche un nom")

while True:
    # entre choix ultilisateur
    choixuser = (input(" Quel est votre choix : "))

    if choixuser == "L":
        liste_repertoire(listerepertoire)
    elif choixuser == "A":
        nouveaunom = input(" entrez nom ")
        nouveaunumero = input(" entrez numero")
        nouveaumail = input(" entre un email")
        ajouter_contact(listerepertoire, nouveaunom, nouveaunumero, nouveaumail)

    elif choixuser == "S":
        contact_a_supprime = input("entre nom du contact a supprimer")
        supprimer_conatct(listerepertoire, contact_a_supprime)
    elif choixuser == "R":
        nomrecherche = input(" entrez le nom recherché :")
        results = rechercher_par_nom(listerepertoire, nomrecherche)
        liste_repertoire(results)

    else:
        print("saisie incorrect")
