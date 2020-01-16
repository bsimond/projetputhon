repertoire = {"brice": "888555666", "marion": "9"}


def liste_repertoire(repertoire):
    for i in repertoire.items():
        print(i)


def rechercher_par_nom(repertoire, nom ):
    results={}
    for key , value in repertoire.items():
        if nom in key:
            ajouter_contact(results, key , value)

    return results




def ajouter_contact(repertoire , nouveaunom, nouveaunumero):

    if rechercher_par_nom(repertoire , nouveaunom) :
         print("contact deja existant")
    else:
         repertoire[nouveaunom] = nouveaunumero


def supprimer_conatct(repertoire, nom):
    del repertoire[nom]


print(" L pour lister, ")
print(" A pour ajouter ")
print(" S pour supprimer")
print(" R pour recherche un nom")



while True:

    choixuser = (input(" Quel est votre choix : "))
    if choixuser == "L":
        liste_repertoire(repertoire)
    elif choixuser == "A":
        nouveaunom = input(" entrez nom ")
        nouveaunumero = input(" entrez numero")
        ajouter_contact(repertoire, nouveaunom, nouveaunumero)

    elif choixuser == "S":
        contact_a_supprime = input("entre nom du contact a supprimer")
        supprimer_conatct(repertoire, contact_a_supprime)
    elif choixuser == "R":
        nomrecherche = input(" entrez le nom recherché :")
        results= rechercher_par_nom(repertoire, nomrecherche)
        liste_repertoire (results)

    else:
        print("saisie incorrect")

