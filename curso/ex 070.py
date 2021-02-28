contV = menor = cont = soma = 0
barat = ''
print('-'*30)
print('{:^30}'.format('Loja Super Baratão'))
print('-'*30)
while True:
    p = str(input('Nome do produto: ')).strip().upper()
    v = float(input('Valor: '))
    soma += v
    cont += 1
    if v > 1000:
        contV += 1
    if cont == 1:
        menor = v
        barat = p
    else:
        if v < menor:
            menor = v
            barat = p
    e = ' '
    while e not in 'SN':
        e = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if e == 'N':
        break
print('{:-^30}'.format(' Fim do Programa '))
print(f'''O total da compra foi R${soma:.2f}
Temos {contV} produtos custando mais de R$1000.00
O produto mais barato foi {barat} que custou R${v:.2f}''')

