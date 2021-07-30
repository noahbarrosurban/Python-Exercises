def ficha(j='<desconhecido>', g=0):
    print(f'O jogador {j} fez {g} gol(s) no campeonato.')


j = input('Nome do jogador: ')
g = input('Número de Gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0

if j.strip() == '':
    ficha(g = g)
else:
    ficha(j, g)