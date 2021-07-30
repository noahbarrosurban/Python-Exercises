dados = {}
gols = []
soma = 0

dados['nome'] = input('Nome do jogador? ')
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

for i in range(1, partidas + 1):
    gols.append(int(input(f'Quantos gols na partida {i}? ')))
dados['gols'] = gols[:]

for i in gols:
    soma += i
dados['total'] = soma

print('-='*30)
print(dados)

print('-='*30)
for k,v in dados.items():
    print(f'O campo {k} tem o valor {v}.')

print('-='*30)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for i in range(0, len(gols)):
    print(f'Na partida {i + 1}, fez {gols[i]}')
print(f'Foi um total de {soma} gols.')



