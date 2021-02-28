p = float(input('Digite seu peso (kg): '))
a = float(input('Digite sua altura (m): '))
imc = p / a ** 2
print('O seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.6 < imc < 25:
    print('PARABÉNS! Você está no peso ideal!')
elif 24.9 < imc < 30:
    print('Você está com sobrepeso!')
elif 29.9 < imc < 40:
    print('Você está com OBESIDADE!')
else:
    print('CUIDADO! Você está com OBESIDADE MÓRBIDA!')


