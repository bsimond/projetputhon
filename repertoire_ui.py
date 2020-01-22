from repertoire_action import *





## fonction pour afficher la liste
## affichage repertoire
def affichage_repertoire(repertoire ):
    for ligne in repertoire:
        print(ligne["nom"], ligne["tel"], ligne["mail"])




def affichage_ajout(repertoire):
    nom = input(" entrez nom ")
    numero = input(" entrez numero")
    mail = input(" entre un email")
    ajouter = ajouter_personne(repertoire , nom, numero, mail)
    if ajouter:
        print("le contact est enregistré")
        affichage_repertoire (repertoire)
    else:
        print("le contact est déjà présent")

def affichage_supprimer(repertoire):
    contact_a_supprime = input("entre nom du contact a supprimer")
    supprimer_personne(repertoire, contact_a_supprime)

while True:
    # entre choix ultilisateur
    print(" L pour lister, ")
    print(" A pour ajouter ")
    print(" S pour supprimer")
    print(" R pour recherche un nom")

    choixuser = (input(" Quel est votre choix : ")).upper()
    repertoire=get_rep()

    if choixuser == "L":
        affichage_repertoire(repertoire)

    elif choixuser == "A":
        affichage_ajout(repertoire)

    elif choixuser == "S":
        affichage_supprimer(repertoire)
        affichage_repertoire(repertoires)

    elif choixuser == "R":
        nomrecherche = input(" entrez le nom recherché :")
        results = chercher_personnes(get_rep(), nomrecherche)
        affichage_repertoire(results)

    else:
        print("saisie incorrect")



