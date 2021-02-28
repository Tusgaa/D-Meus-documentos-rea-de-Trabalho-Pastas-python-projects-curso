from random import randint
cont = 0
while True:
    print('=-'*8)
    print('PAR OU ÍMPAR')
    print('=-'*8)
    j = int(input('Escolha um valor: '))
    s = str(input('A soma dos valores escolhidos será par ou ímpar? [P/I] ')).strip().upper()[0]
    pc = randint(0, 10)
    print('-'*15)
    if (j + pc) % 2 == 0:
        print(f'Você jogou {j} e o computador {pc}. Total de {j+pc} DEU PAR')
        s1 = 'P'
        if s1 == s:
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            cont += 1
        elif s1 != s:
            print('Você PERDEU!')
            break
    elif (j + pc) % 2 != 0:
        print(f'Você jogou {j} e o computador {pc}. Total de {j+pc} DEU ÍMPAR')
        s1 = 'I'
        if s1 == s:
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            cont += 1
        elif s1 != s:
            print('Você PERDEU!')
            break
print(f'GAME OVER! Você venceu {cont} vezes.')

