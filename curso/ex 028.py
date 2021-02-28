'''n = int(input('Estou pensando em um número, tente adivinha-lo: '))
print('Processando...')
if n == 3:
    print('Parabéns você acertou!')
else:
    print('Tente novamente.')'''
from random import randint
pc = randint(0,5) #escolha do computador
print('-=-'*25)
print('Estou pensando em um número entre 0 e 5. Tente adivinhar ...')
pessoa = int(input('Digite o número escolhido: '))
if pessoa == pc:
    print('Parabéns, você acertou! O número escolhido foi o {}'.format(pc))
else:
    print('Você errou, o número escolhido foi o {}, tente novamente.'.format(pc))




