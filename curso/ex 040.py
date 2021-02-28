print('\33[1;33m-=-'*7)
print('\33[1;33mAnalisador de médias')
print('\33[1;33m-=-'*7, '\33[m')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('''\33[1;33mAnalisando as médias 
.........
.....
...
\33[m''')
if m > 7:
    print('''Tirando {} e {} a média é {:.2f}!
Você foi \33[1;32mAPROVADO\33[m!'''.format(n1, n2, m))
elif m < 5:
    print('''Tirando {} e {} a média é {:.2f}!
Você foi \33[1;31mReprovado\33[m!'''.format(n1, n2, m))
elif 7 > m > 5:
    print('''Tirando {} e {} a média é {:.2f}!
Você está de \33[1;33mRECUPERAÇÃO\33[m!'''.format(n1, n2 , m))
