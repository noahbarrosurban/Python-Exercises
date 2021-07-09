'''primeiro = int(input('Digite o priemiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print(c, '> ', end='')
print('Acabou')
'''

primeiro = int(input('Digite o priemiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} ', end='')
    termo += razão
    cont += 1
print('...')