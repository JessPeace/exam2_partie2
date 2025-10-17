from datetime import *

#je sais pas pourquoi le code focntionne pas. je vais dans mes notes et il y a rien qui débloque.

horraire=[ '6:14', '7:44', '9:14', '10:44', '12:14', '13:44', '15:14', '16:44', '18:14' , '19:44', '21:14' ]

'''aujourdhui = datetime.now()
print(aujourdhui.strftime('il est %H:%M '))'''
heure = int(input('quel heure est til?'))
minutes = 90

def heure_de_passage(heure, minutes):
    '''
    fonction qui vas calculer les minutes restants le prochain passage du bus hanté:
    :param intervales: 90 minutes
    :param minutes: minutes avant le prochain passage
    :return: minutes restants avant le prochain passage du bus hanté.
    '''
    try:
        intervales = (heure-minutes)
    except IndentationError and TypeError:
        if  intervales<= 15:                    #là j'essaie de faire en sorte que python fasse une soustraction des minutes sur l'heure pour renvoiller le temps restant.
            print(f" l'autobuss passe à [{horraire}]")
            print(f"le buss arriveras dans [{intervales}] minutes.")
    if intervales <=30:
        print(f" l'autobuss passe à [{horraire}]")
        print(f"le buss arriveras dans [{intervales}] minutes.")
        print(intervales)

#il y a rien qui fontionne. je fais mon possible mais rien fonctionne sauf mes print.

if __name__ == "__main__":
    minutes = 90
    print("l'horraire de passage du buss hanté est:\n6:14\n7:44\n9:14\n10:44\n12:14\n13:44\n15:14\n16:44\n18:14\n19:44\n21:14.")
    heure_de_passage(heure,minutes)

