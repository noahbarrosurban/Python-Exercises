from random import randint
from operator import itemgetter

dic = {'player1': randint(1, 6), 'player2': randint(1, 6),
       'player3': randint(1, 6), 'player4': randint(1, 6),}

ranking = {}

print('Valores sorteados:')
for k, v in dic.items():
    print(f'O {k} tirou {v} no dado.')

print('Ranking dos jogadores:')
ranking = sorted(dic.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
