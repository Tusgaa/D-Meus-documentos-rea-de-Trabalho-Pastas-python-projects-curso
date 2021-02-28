print('='*30)
print('     10 termos de uma PA')
print('='*30)
pn = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = pn + 10 * r
for c in range(pn, d, r):
    print('{} '.format(c), end='→ ')
print('FIM')

