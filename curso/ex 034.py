s = float(input('Digite o valor do salário: '))
if s < 1250:
    print('O seu salário pssará a ser de R${:.2f}.'.format(s + (15/100 * s)))
else:
    print('O seu salário passará a ser de R${:.2f}.'.format(s + (10/100 * s)))

