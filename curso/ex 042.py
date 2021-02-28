#a = float(input('Primeiro segmento: '))
#b = float(input('Segundo segmento: '))
#c = float(input('Terceiro segmento: '))
#if a < b + c and b < a + c and c < b + a and a == b and b == c and c == a:
#    print('''O triângulo existe {:.1f}, {:.1f}, {:.1f} existe!
#Os segmentos acima podem formar um triângulo ISÓCELES.'''.format(a, b, c))
#elif a == b and b == c and a < b + c and b < a + c and c < b + a:
#    print('''O triângulo {:.1f}, {:.1f}, {:.1f} existe!
#Os segmentos acima podem formar um triângulo EQUILÁTERO.'''.format(a, b, c))
#elif a != b and b != c and c != a and a < b + c and b < a + c and c < b + a:
#   print('''O triângulo {:.1f}, {:.1f}, {:.1f} existe!
#Os segmentos acima podem formar um triângulo ESCALENO.'''.format(a, b, c))
#else:
#    print('Com os segmentos informados o triângulo \33[1;31mNÃO EXISTE!')

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < b + a:
    print('O triângulo existe {:.1f}, {:.1f}, {:.1f} \33[1;32mEXISTE!\33[m'.format(a, b, c), end=' ')
    if a == b == c:
        print('Formando um triângulo EQUILÁTERO!')
    elif a != b != c != a:
        print('Formando um triângulo ESCALENO!')
    else:
        print('Formando um triângulo ISÓCELES!')
else:
    print('Com os segmentos informados o triângulo \33[1;31mNÃO EXISTE!')





