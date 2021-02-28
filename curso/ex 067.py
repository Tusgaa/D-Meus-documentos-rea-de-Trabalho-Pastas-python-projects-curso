n = 1
while True:
    print('-'*35)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*35)
    if n < 0:
        break
    for num in range(1,  11):
        print(f'{n} x {num} = {n*num}')
print('Programa de tabuada encerrado! Volte sempre!')
