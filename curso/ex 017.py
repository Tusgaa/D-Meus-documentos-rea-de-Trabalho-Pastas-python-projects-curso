'''from math import pow, sqrt
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimeto do cateto adjacente: '))
co1 = pow(co,2)
ca1 = pow(ca,2)
print('Com estes valores a hipotenusa irá medir: {:.2f}'.format(sqrt(co1+ + ca1)))'''

from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
print('Então o valor da hipotenusa será de: {:.2f}'.format(hypot(co, ca)))








