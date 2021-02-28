print('Gerador de PA')
print('-='*7)
cont = 1
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
while cont <= 10:
    print('{} →'.format(n), end=' ')
    n += r
    cont += 1
print('FIM!')