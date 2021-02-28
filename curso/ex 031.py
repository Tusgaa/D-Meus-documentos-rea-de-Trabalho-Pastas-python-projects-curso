d = float(input('Qual a distância da viagem? '))
v = d * 0.50
if d<200:
    print('O valor da viagem será de R${:.2f}.'.format(v))
else:
    print('O valor da viagem será de R${:.2f}.'.format(d*0.45))
