import random

def pregunta(x):
    numero_random=random.randint(1,x)
    pregunta=0
    while pregunta!= numero_random:
        pregunta=int(input(f'pregunta un numero entre 1 y{x}:'))
        if pregunta < numero_random:
            print('siga participando , es muy bajo')
        elif pegunta > numero_random:
            print('siga participando , es muy alto')


            print(f'correcto!! , has acertado{numero_random}')


def pregunta_computadora(x):
    bajo=1
    alto=x
    feedback=''
    while feedback!= 'c' and low !=alto:

        if low!= high:
            pregunta='muy bajo'
        pregunta = random.randint(bajo,alto)
        feedback = input('f{es pregunta} muy alto(h),muy bajo(c), correcto (s)')
    else:
        pregunta= bajo
        if feedback=='h':
            alto=pregunta - 1
        elif feedback== 'l':
            bajo = pregunta +1
    print(f'si , la computadora gano!!')

    computadora_pregunta(10)
