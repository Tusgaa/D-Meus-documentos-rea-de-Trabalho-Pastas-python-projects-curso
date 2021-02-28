times = ('Internacional', 'Atlético-MG', 'Flamengo', 'São Paulo', 'Fluminense', 'Palmeira', 'Santos', 'Grêmio',
         'Bahia', 'Sport Recife', 'Corinthians', 'Fortaleza', 'Ceará SC', 'Atlético-GO', 'Coritiba', 'Bragantino-SP',
         'Botafogo', 'Vasco da Gama', 'Athletico-PR', 'Goiás')
print('Lista de times do Brasileirão: ', times)
print('-='*15)
print('Os 5 primeiros são: ', times[0:6])
print('-='*15)
print('Os 4 últimos são: ', times[-4:])
print('-='*15)
print('Times em ordem alfabética: ', sorted(times))
print('-='*15)
print(f'O Corinthians está na {times.index("Corinthians")+1}ª posição')
