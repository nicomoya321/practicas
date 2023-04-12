import random

def play():
    usuario=input("'r'para piedra, 'p' para papel ,'t' para tijeras")
    computadora=random.choice(['r','p','s'])

    if usuario==computadora:
        return'empate'

    if gano(usuario,computadora):
        return 'tu ganas '
    return 'pierdes'


def gano(jugador , oponente):
    if jugador == 'r' and oponente == 's' or jugador == 's' and oponente == 'p' or jugador == 'p' and oponente == 'r':
        return true
    else:
        pass

print(play)
