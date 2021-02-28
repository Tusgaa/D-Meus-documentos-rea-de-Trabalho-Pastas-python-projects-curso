a = float(input('Digite o valor do comprimento do primeiro lado: '))
b = float(input('Digite o valor do comprimineto do segundo lado: '))
c = float(input('Digite o valor do comprimento do segundo lado: '))
if a < b + c and b < a + c and c < b + a:
    print('O triângulo existe {}, {}, {} existe!'.format(a, b, c))
else:
    print('O triângulo existe {}, {}, {} não existe!'.format(a, b, c))

