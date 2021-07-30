lista = []
res = ' '
while True:
    lista.append(int(input('Digite um valor: ')))

    res = input('Quer continuar? [S/N] ').strip().upper()[0]

    if res not in 'S':
        break

print(f'Você digitou {len(lista)} elementos.')

lista.sort(reverse=True)

print(f'Os valores em ordem decrescente são {lista}')

if 5 in lista:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
