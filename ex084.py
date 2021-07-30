pessoas = []
dados = []
resp = ''
maior = menor = 0
nomemaior = nomemenor = ''

while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
        nomemaior = nomemenor = dados[0]
    else:
        if dados[1] > maior:
            maior = dados[1]
            nomemaior = dados[0]
        if dados[1] < menor:
            menor = dados[1]
            nomemenor = dados[0]

    pessoas.append(dados[:])
    dados.clear()

    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break

print(f'Ao todo você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior} . Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'O menor peso foi de {menor} . Peso de ',end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}')