pessoas = []
individual = {}
cont = 0
soma = 0
while True:
    individual['nome'] = (input('Nome: '))
    individual['genero'] = (input('Genero: [M/F] '))
    individual['idade'] = (int(input('Idade: ')))

    soma += individual['idade']

    pessoas.append(individual.copy())
    individual.clear()

    cont += 1

    resp = input('Quer continuar? [S/N]')
    if resp in 'Nn':
        break


print(pessoas)
print(f'- O grupo tem {cont} pessoas.')
print(f'- A média de idade é de {soma / cont}')

print(f'- As mulheres cadastradas foram ', end='')
for i in pessoas:
    if i['genero'] in 'Ff':
        print(f'{i["nome"]} ', end='')
print()

print(f'- As pessoas que estão acima da média: ')
for i in pessoas:
    if i['idade'] >= soma / cont:
        print('', end='')
        for k, v in i.items():
            print(f'{k} = {v}; ', end='')
        print()



