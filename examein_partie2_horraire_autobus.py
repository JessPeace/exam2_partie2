from datetime import *

print('lhorraire de passage du buss hanté est:\n6:14\n7:44\n9:14\n10:44\n12:14\n13:44\n15:14\n16:44\n18:14\n19:44\n21:14.')

'''aujourdhui = datetime.now()
print(aujourdhui.strftime('il est %H:%M '))'''

#heure=input('quel heure est til?')
heure=('12:10') ##test##

def heure_de_passage(minutes):
    '''
    fonction qui vas calculer les minutes restants le prochain passage du bus hanté:
    :param intervales: 90 minutes
    :param minutes: minutes avant le procchain passage
    :return: minutes restants avant le prochain passage du bus hanté.
    '''
    intervales = ( heure % minutes )
    if intervales <= 15:
        print('le buss arriveras dans 15 minutes.')
    elif intervales <=30:
        print('le buss arriveras dans 30 minutes.')
        return intervales



#abs(aujourdhui.date() - la_date):

if __name__ == "__main__":

    heure_de_passage(minute=90)

    #là j'essaie de faire en sorte que python fasse une soustraction des minutes sur l'heure