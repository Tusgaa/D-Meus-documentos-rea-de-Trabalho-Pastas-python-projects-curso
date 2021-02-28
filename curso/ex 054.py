cont1 = 0
cont2 = 0
from datetime import date
for c in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = date.today().year - nasc
    if idade >= 18:
        cont1 += 1
    elif idade <= 17:
        cont2 += 1
print('Tivemos {} pessoas maiores de idade!'.format(cont1))
print('Tivemos {} pessoas menores de idade!'.format(cont2))
