from random import randint
cont = 0
print(''' Sou seu computador...
Acabei de escolher um número entre 0 e 10.
Você consegue adivinhar que número foi o que eu escolhi?''')
n = int(input('Qual o seu palpite: '))
c = randint(0, 10)
while n != c:
    if n < c:
        n = int(input('MAIS... Tente novamente: '))
        cont += 1
    elif n > c:
        n = int(input('MENOS... Tente novamente: '))
        cont += 1
print('PARABÉNS! Você acertou com {} tentativas.'.format(cont))


