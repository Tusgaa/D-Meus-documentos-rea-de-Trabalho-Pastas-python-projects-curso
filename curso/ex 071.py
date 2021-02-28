print('='*20)
print('{:^20}'.format('Banco Tusga'))
print('='*20)
v = int(input('Que valor você deseja sacar? R$'))
tot = v
ced = 50
contced = 0
while True:
    if tot >= ced:
        tot -= ced
        contced += 1
    else:
        if contced > 0:
            print(f'Total de {contced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        contced = 0
        if tot == 0:
            break
print('='*20)
print('Obrigado e volte sempre ao Banco Tusga.')
