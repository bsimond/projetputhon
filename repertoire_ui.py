from repertoire_action import *

repertoire = [{"nom": "brice", "tel": "88555666", "mail": "brice@gmail.com"},
                   {"nom": "marion", "tel": "4557682", "mail": "marion@gmail.com"},
                   {"nom": "marcin", "tel": "454545", "mail": " marcin@gmail.Com"}]



## fonction pour afficher la liste
def liste_repertoire(repertoire):
    for ligne in repertoire:
        print(ligne["nom"], ligne["tel"], ligne["mail"])




def affichage_ajout(repertoire):
    nom = input(" entrez nom ")
    numero = input(" entrez numero")
    mail = input(" entre un email")
    ajouter = ajouter_contact(repertoire, nom, numero, mail)
    if ajouter:
        print("le contact est enregistré")
    else:
        print("le contact est déjà présent")

def affichage_supprimer(repertoire):
    contact_a_supprime = input("entre nom du contact a supprimer")
    supprimer_contact(repertoire, contact_a_supprime)

while True:
    # entre choix ultilisateur
    choixuser = (input(" Quel est votre choix : ")).upper()

    if choixuser == "L":
        liste_repertoire(repertoire)

    elif choixuser == "A":
        affichage_ajout(repertoire)

    elif choixuser == "S":
        affichage_supprimer(repertoire)

    elif choixuser == "R":
        nomrecherche = input(" entrez le nom recherché :")
        results = rechercher_par_nom(repertoire, nomrecherche)
        liste_repertoire(results)

    else:
        print("saisie incorrect")



print(" L pour lister, ")
print(" A pour ajouter ")
print(" S pour supprimer")
print(" R pour recherche un nom")
