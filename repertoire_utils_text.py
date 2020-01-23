import json
# repertoire = [{"nom": "brice", "tel": "88555666", "mail": "brice@gmail.com"},
#                    {"nom": "marion", "tel": "4557682", "mail": "marion@gmail.com"},
#                    {"nom": "marcin", "tel": "454545", "mail": " marcin@gmail.Com"}]

# fichier = open("repertoire.txt", "w")
# repertoirestr = json.dumps(repertoire)
# fichier.write(repertoirestr)
# fichier.close()





def get_rep():
     fichier=open("repertoire.txt", "r")
     repertoire=json.loads(fichier.read())
     fichier.close()
     return repertoire


def append_rep (repertoire,personne ):
    repertoire.append(personne)
    fichier = open("repertoire.txt", "w")
    repertoirestr = json.dumps(repertoire)
    fichier.write(repertoirestr)
    fichier.close()
    return repertoire

def del_rep ( repertoire, personne):
    repertoire.remove(personne)
    fichier = open("repertoire.txt", "w")
    repertoirestr = json.dumps(repertoire)
    fichier.write(repertoirestr)
    fichier.close()
    return repertoire





