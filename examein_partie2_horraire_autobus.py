#from datetime import *

#je sais pas pourquoi le code fonctionne pas. je vais dans mes notes et il y a rien qui débloques.

horraire=[ '6h14', '7h44', '9:14', '10:44', '12:14', '13:44', '15:14', '16:44', '18:14' , '19:44', '21:14' ]
#ça c'est la liste pour python.^^^^

##tests## heure= '12:12'
heure = (input('quel heure est til?'))
#je veux vraiment que python figure que j'essaie de lui donner une valeur avec l'utilisateur mais il comprends pas c'est quoi.
# Et sa me rends folle.
minutes = 90
#je regades toutes mes lignes et il y a rien qui cloche.....
#je sais que j'ai un problème de traduction mais je sais pas où.
def heure_de_passage(heure, minutes, intervales):
    '''
    fonction qui vas calculer les minutes restants le prochain passage du bus hanté:
    :param intervales: 90 minutes
    :param minutes: minutes avant le prochain passage
    :return: minutes restants avant le prochain passage du bus hanté.
    '''
    try:
        intervales = (heure-minutes)
    except IndentationError and TypeError:
        if  intervales<= 15:
#là j'essaie de faire en sorte que python fasse une soustraction des minutes sur l'heure pour renvoiller le temps restant.
            print(f" l'autobuss passe à [{horraire}]")
            print(f"le buss arriveras dans [{intervales}] minutes.")
    if intervales <=30:
        print(f" l'autobuss passe à [{horraire}]")
        print(f"le buss arriveras dans [{intervales}] minutes.")
        return intervales

#il y a rien qui fontionne. je fais mon possible mais rien fonctionne sauf mes print.

if __name__ == "__main__":
    minutes = 90
    print("l'horraire de passage du buss hanté est:\n6:14\n7:44\n9:14\n10:44\n12:14\n13:44\n15:14\n16:44\n18:14\n19:44\n21:14.")
    #ça c'est pour montrer à l'utilisateur l'horraire du bus, c'est pas une liste pour python. ^^^^
    heure_de_passage(heure,minutes,intervales)

#'TypeError: unsupported operand type(s) for -: 'str' and 'int'
# je comprends pas comment réperer cette erreur là.
