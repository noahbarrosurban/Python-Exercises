lista = ('Xbox Series S', 2659.05,
         'Xbox Series X', 6788.99,
         'Playstation', 6450.00,
         'Nintendo Switch', 2207.91)

print('-' * 40)
print(f'{"PREÇOS 2021":^40}')
print('-' * 40)

for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]:.<30}', end='')
    else:
        print(f'R$ {lista[i]:.>7.2f}')

print('-' * 40)