print('Gerador de PA')
print('-='*7)
cont = 1
pn = int(input('Primeiro termo: '))
r = int(input('Razão: '))
tot = 0
n = 10
while n != 0:
    tot += n
    while cont <= tot:
        print('{} →'.format(pn), end=' ')
        pn += r
        cont += 1
    print('PAUSA')
    n = int(input('Quantos termos você quer mostrar a mais? '))
print('A progressão foi finalizada com {} termos mostrados.'.format(tot))

