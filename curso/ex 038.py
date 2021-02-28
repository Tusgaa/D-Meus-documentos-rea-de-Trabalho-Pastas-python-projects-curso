n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n1 > n2:
    print('{} é maior que {}.'.format(n1, n2))
elif n1 < n2:
    print('{} é menor que {}.'.format(n1, n2))
elif n1 == n2:
    print('Os dois valores são iguais.')
