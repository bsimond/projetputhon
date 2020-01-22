repertoire = [{"nom": "brice", "tel": "88555666", "mail": "brice@gmail.com"},
                   {"nom": "marion", "tel": "4557682", "mail": "marion@gmail.com"},
                   {"nom": "marcin", "tel": "454545", "mail": " marcin@gmail.Com"}]

## fonction get_rep qui retournera une dictionnaire avec un répertoire téléphonique
def get_rep():
    return repertoire
##  def append_rep qui ajoutera une personne au repertoire
def append_rep (repertoire,personne ):
    repertoire.append (personne)


## def del_rep qui supprimera une personne du repertoire
def del_rep (repertoire,personne ):
  repertoire.remove(personne)