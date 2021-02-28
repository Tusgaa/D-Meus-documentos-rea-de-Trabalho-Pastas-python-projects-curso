frase = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculo fica: {}'.format(frase.upper()))
print('Seu nome em minúsculo fica: {}'.format(frase.lower()))
print('O número de letras que seu nome possui é: {}' .format(len(frase) - frase.count(' ')))
separado = frase.split()
print('Seu primeiro nome é {} e possui {} letras.'.format(separado[0], len(separado[0])))

