from random import randint
l = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opções são:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
j = int(input('Qual é a sua jogada? '))
print('-='*15)
print('O computador escolheu {}!'.format(l[pc]))
print('O jogador jogou {}!'.format(l[j]))
print('-='*15)
if pc == 0: #PC jogando pedra
    if j == 0:
        print('Ocorreu um EMAPTE!')
    elif j == 1:
        print('O jogador GANHOU!')
    elif j == 2:
        print('O computador GANHOU!')
    else:
        print('Jogada Inválida!')
elif pc == 1: #PC jogando papel
    if j == 0:
        print('O computadro GANHOU!')
    elif j == 1:
        print('Ocorreu um EMPATE!')
    elif j == 2:
        print('O jodador GANHOU!')
    else:
        print('Jogada Inválida!')
elif pc == 2: #PC jogando tesoura
    if j == 0:
        print('O jogador GANHOU!')
    elif j == 1:
        print('O computador GANHOU!')
    elif j == 2:
        print('Ocorreu um EMPATE!')
    else:
        print('Jogada Inválida!')
print('JOGUE NOVAMENTE!')
