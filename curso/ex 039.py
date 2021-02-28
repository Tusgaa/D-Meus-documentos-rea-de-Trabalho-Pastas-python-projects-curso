a = int(input('Ano de nascimento: '))
if a > 2002:
    print('''Quem nasceu em {} tem {} anos em 2020.
Ainda faltam {} para o alistamento.
Seu alistamento será em {}.'''.format(a, 2020 - a, 18 - (2020 - a), (2020) + 18 - (2020 - a)))
elif a < 2002:
    print('''Quem nasceu em {} tem {} anos em 2020.
Você deveria ter se alistado há {} anos.
Seu alistamento foi em {}.'''.format(a, 2020 - a, (2020 - a) - 18,  2020 - ((2020 - a) - 18)))
elif a == 2002:
    print('''Quem nasceu em {} tem 18 anos em 2020.
Você tem que se alistar imediatamente!'''.format(a))

