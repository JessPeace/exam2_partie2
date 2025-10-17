from datetime import *



horraire=[ '6:14', '7:44', '9:14', '10:44', '12:14', '13:44', '15:14', '16:44', '18:14' , '19:44', '21:14' ]

'''aujourdhui = datetime.now()
print(aujourdhui.strftime('il est %H:%M '))'''


#heure = ('12:10') #test##
minutes = 90

def heure_de_passage(heure, minutes):
    '''
    fonction qui vas calculer les minutes restants le prochain passage du bus hanté:
    :param intervales: 90 minutes
    :param minutes: minutes avant le procchain passage
    :return: minutes restants avant le prochain passage du bus hanté.
    '''
    heure== input('quel heure est til?')
    intervales = (heure-minutes)
    if intervales <= 15:
        print(f" l'autobuss passe à [{horraire}]")
        print(f"le buss arriveras dans [{intervales}] minutes.")
    elif intervales <=30:
        print(f" l'autobuss passe à [{horraire}]")
        print(f"le buss arriveras dans [{intervales}] minutes.")
        print(intervales)
        return intervales



#abs(aujourdhui.date() - la_date):

if __name__ == "__main__":
    print("l'horraire de passage du buss hanté est:\n6:14\n7:44\n9:14\n10:44\n12:14\n13:44\n15:14\n16:44\n18:14\n19:44\n21:14.")
    heure_de_passage(heure, 90)

    #là j'essaie de faire en sorte que python fasse une soustraction des minutes sur l'heure