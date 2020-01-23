import repertoire_action as action

## fonction pour afficher la liste
## affichage repertoire


def affichage_repertoire(repertoire):
    contact= action.lister_tous_les_contact(repertoire)
    print(contact)





def affichage_ajout(repertoire):
    nom = input(" entrez nom :  ")
    numero = input(" entrez numero : ")
    mail = input(" entre un email : ")
    resultat_ajouter = action.ajouter_personne(repertoire , nom, numero, mail)
    if resultat_ajouter:
        print("le contact est enregistré")
        affichage_repertoire (repertoire)
    else:
        print("le contact est déjà présent")

def affichage_supprimer(repertoire):
    contact_a_supprime = input("entre nom du contact a supprimer : ")
    action.supprimer_personne(repertoire, contact_a_supprime)





while True:
    # entre choix ultilisateur
    print(" L pour lister, ")
    print(" A pour ajouter ")
    print(" S pour supprimer")
    print(" R pour recherche un nom")

    choixuser = (input(" Quel est votre choix : ")).upper()
    repertoire=action.get_rep()

    if choixuser == "L":
        affichage_repertoire(repertoire)

    elif choixuser == "A":
        affichage_ajout(repertoire)

    elif choixuser == "S":
        affichage_supprimer(repertoire)
        affichage_repertoire(repertoire)




    elif choixuser == "R":
        nomrecherche = input(" entrez le nom recherché :")
        results = chercher_personnes(repertoire, nomrecherche)
        affichage_repertoire(results)

    else:
        print("saisie incorrect")



