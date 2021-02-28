from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
escolha = 0
while escolha != 6:
    sleep(2)
    print('=-' * 15)
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] dividir
    [ 6 ] sair do programa''')
    escolha = int(input('>>>>> Qual é sua escolha? '))
    if escolha == 1:
       soma = n1 + n2
       print('A soma entre {} + {} é {}.'.format(n1, n2, soma))
    elif escolha == 2:
        multiplicar = n1 * n2
        print('O resultado de {} x {} = {}'.format(n1, n2, multiplicar))
    elif escolha == 3:
        if n1 > n2:
            print('{} é o maior número!'.format(n1))
        elif n1 == n2:
            print('Os números escolhidos são iguais')
        else:
            print('{} é o maior número!'.format(n2))
    elif escolha == 4:
        print('Informe os valores novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif escolha == 5:
        dividir = n1 / n2
        print('{} dividido por {} é igual a {:.2f}'.format(n1, n2, dividir))
    elif escolha == 6:
        print('Finalizando...')
print('Fim do programa! Volte sempre!')




