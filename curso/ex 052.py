n = int(input('Digite um número: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\33[33m', end='')
        total += 1
    else:
        print('\33[31m', end='')
    print(c, end=' ')
print('\n\33[mO número {} foi divisível {} vezes'.format(n, total))
if total == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele não é PRIMO')










