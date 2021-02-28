n = int(input('Digite um número inteiro: '))
print('''Escolha uma das opções de conversão:
[ 1 ] converter para BINÁRIO 
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
n1 = int(input('Sua opção escolhida foi: '))
if n1 == 1:
    print('{} convertido para BINÁRIO é igual a: {}'.format(n, bin(n)[2:]))
elif n1 == 2:
    print('{} convertido para OCTAL é igual a: {}'.format(n, oct(n)[2:]))
else:
    print('{} convertido para HEXADECIMAL é igual a: {}'.format(n, hex(n)[2:]))





