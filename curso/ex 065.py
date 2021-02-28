cont = soma = med = 0
r = 'S'
while r == 'S':
    num = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
med = soma / cont
soma += num
print('Você digitou {} números e a média foi {:.2f}!'.format(cont, med))
print('O maior valor foi {} e o menor foi {}!'.format(maior, menor))
