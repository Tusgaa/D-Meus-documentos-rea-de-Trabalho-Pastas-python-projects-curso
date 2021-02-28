print('-'*23)
print('Sequência de Fibonacci')
print('-'*23)
n = int(input('Quantos termos você quer mostrar? '))
print('-'*35)
cont = 2
t1 = 0
t2 = 1
if n == 0:
    n = int(input(('O valor inserido é \033[31mINVÁLIDO\033[m! Insira outro valor: ')))
elif n == 1:
    print('0', end=' ')
elif n > 1:
    print('{} → {}'.format(t1, t2), end=' ')
    while cont != n:
        t3 = t1 + t2
        print('→ {}'.format(t3), end=' ')
        t1 = t2
        t2 = t3
        cont += 1
print('→ FIM!')
