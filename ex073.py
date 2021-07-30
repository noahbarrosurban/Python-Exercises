times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')

print('=' * 100)
print(f'Os 5 primeiros colocados são {times[:5]}.')

print('=' * 100)
print(f'Os últimos 4 colocados são {times[-4:]}.')

print('=' * 100)
print(f'Os times em ordem alfabética são {sorted(times)}.')

print('=' * 100)
print(f"O time Chapecoense está na posição {times.index('Chapecoense')+1}.")
print('=' * 100)