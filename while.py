'''i = 1
while i <= 10:
    print(i)
    i += 1'''
import random
numero_aleatorio = random.randint(0, 5)
cont = 0
lim = 3
while True:
    palpite = int(input('Qual é o número que eu estou pensando? '))
    if palpite == numero_aleatorio:
        print('Parabens, você acertou!')
        break
    elif palpite!= numero_aleatorio:
        if cont < lim:
            print(f'Você errou, tente novamente...Você possui mais {lim - cont} chances')
            cont += 1
        else:
            print('Você errou! Acabou suas chances =(')
            break
