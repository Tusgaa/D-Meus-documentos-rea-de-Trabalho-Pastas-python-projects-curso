print('='*13, 'Lojas Tusga', '='*13)
v = float(input('Insira o valor: '))
print('''FORMAS DE PAGAMENTO
[ 1 ] À Vista dinheiro/cheque
[ 2 ] À Vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
o = int(input('Qual será a forma de pagamento? '))
if o == 1:
    print('Sua compra de R${:.2f}, à vista no dinheiro ou cheque tem 10% de desconto'.format(v), end=' ')
    print('e irá custar R${:.2f}!'.format(v - v * (10/100)))
elif o == 2:
    print('Sua compra de R${:.2f}, à vista no cartão tem 5% de desconto'.format(v), end=' ')
    print('e irá custar R${:.2f}!'.format(v - v * (5/100)))
elif o == 3:
    print('Sua compra de R${:.2f}, em 2x no cartão não terá juros!'.format(v))
else:
    x = int(input('Em quantas vezes? '))
    print('Sua compra de {:.2f} pacelada custará {}x de R${} COM JUROS!'.format(v, x, (v + v * (20/100)) / x), end=' ')
    print('Custando no total R${:.2f}.'.format(v + v * (20/100)))
print('OBRIGADO PELA PREFERÊNCIA. VOLTE SEMPRE!')



