time = []
dados = {}
gols = []
soma = 0


while True:
    dados.clear()
    gols.clear()

    dados['nome'] = input('Nome do jogador? ')
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

    for i in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {i + 1}? ')))
        dados['gols'] = gols[:]

    time.append(dados.copy())

    resp = input('Quer continuar? [S/N]')
    if resp in 'Nn':
        break


print('-='*30)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*30)

while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar]'))
    if busca == 999:
        break
    if busca > len(time):
        print(f'ERRO! Não existe jogador código {busca}!')
    else:
        print(f'Levantamento do jogador {time[busca]["nome"]}!')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i} fez {g} gols.')
        print('-=' * 30)