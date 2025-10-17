from datetime import *

print('lhorraire de passage du buss hanté est:\n6:14\n7:44\n9:14\n10:44\n12:14\n13:44\n15:14\n16:44\n18:14\n19:44\n21:14.')

aujourdhui=datetime.today()
print(aujourdhui.strftime('il est %H:%M '))


def heure_de_passage(intervales, minutes):
    '''
    foonction qui vas calculer les minutes restants le prochain passage du bus hanté:
    :param intervales: 90 minutes
    :param minutes: minutes avant le procchain passage
    :return: minutes restants avant le prochain passage du bus hanté.
    '''
    intervales = abs(aujourdhui.date() - heure_de_passage )
    print(intervales.minutes-90,'minutes avant le passage du buss hanté.')


if __name__ == "__main__":

