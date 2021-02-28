print('\33[1;33m-=-'*12)
print('\33[1;33mAnalisador de empréstimo bancário')
print('\33[1;33m-=-'*12, '\33[m')
v = float(input('Digite o valor da casa: '))
s = float(input('Digite o seu salário: '))
a = float(input('Digite em quantos anos o pagamento será feito: '))
p = (v / (a*12))
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(v, a, p))
if p > s*(30/100):
    print('\33[1;31mO empréstimo não pode ser realizado!''\33[m')
else:
    print('\33[1;34mO empréstimo pode ser realizado!''\33[m')


