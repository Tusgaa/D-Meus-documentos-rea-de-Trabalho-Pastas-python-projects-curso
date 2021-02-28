f = str(input('Digite uma frase: ')).strip().lower()
print('A letra E apareceu {} vezes.'.format(f.count('e')))
print('A primeira letra E apareceu na posição {}'.format(f.find('e')+1))
print('Já a última letra E apareceu na posição {}'.format(f.rfind('e')+1))

