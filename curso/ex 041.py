from datetime import date
atual = date.today().year
a = int(input('Ano de nascimento: '))
i = atual - a
print('O atleta tem {} anos.'.format(i))
if i < 10:
    print('Classificação: MIRIM')
elif 9 < i < 15:
    print('Classificação: INFANTIL')
elif 14 < i < 20:
    print('Classificação: Junior')
elif 19 < i < 30:
    print('Classificação: SÊNIOR')
elif i > 30:
    print('Classificação: MASTER')

