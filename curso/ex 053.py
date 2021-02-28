frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('A frase ao contrário fica {}'.format(inverso))
if inverso == junto:
    print('Esta frase digitade é um palíndromo!')
else:
    print('Esta frase digitada não é um palíndromo!')
