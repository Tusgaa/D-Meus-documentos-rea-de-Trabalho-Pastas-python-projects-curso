v = int(input('Qual a velocidade atual do carro? '))
if v > 80:
    print('Você ultrapassou o limite de 80 km/h, portanto terá que pagar uma multa de R${:.2f}!'.format((v-80)*7))
print('Tenha um bom dia! Dirija com segurança!')


