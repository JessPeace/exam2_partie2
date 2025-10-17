from datetime import *

print('lhorraire de passage du buss hanté est:\n6:14\n7:44\n9:14\n10:44\n12:14\n13:44\n15:14\n16:44\n18:14\n19:44\n21:14.')

'''aujourdhui = datetime.now()
print(aujourdhui.strftime('il est %H:%M '))'''

heure=input('quel heure est til?')

def heure_de_passage(intervales, minutes, heure):
    '''
    fonction qui vas calculer les minutes restants le prochain passage du bus hanté:
    :param intervales: 90 minutes
    :param minutes: minutes avant le procchain passage
    :return: minutes restants avant le prochain passage du bus hanté.
    '''
    intervales = ( minutes - heure )
    print('f' {intervales} 'avant le passage du buss hanté.') #là je veux que python imprime le retour de l'intervale en texte.
    return intervales


#abs(aujourdhui.date() - la_date):

if __name__ == "__main__":

    heure_de_passage(minutes=90,aujourdhui) #là j'essaie de faire en sorte que python fasse une soustraction des minutes sur l'heure