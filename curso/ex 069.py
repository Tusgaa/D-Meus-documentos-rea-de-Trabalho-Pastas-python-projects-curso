contM = contH = contI = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    i = int(input('IDADE: '))
    s = ' '
    while s not in 'MF':
        s = str(input('SEXO: [M/F] ')).upper().strip()[0]
    if i >= 18:
        contI += 1
    if s in 'M':
        contH += 1
    if s in 'F' and i < 20:
        contM += 1
    e = ' '
    while e not in 'SN':
        e = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if e == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos: {contI}
Ao todo temos {contH} homens cadastrados
E temos {contM} mulheres com menos de 20 anos''')
