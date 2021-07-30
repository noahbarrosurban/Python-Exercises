def area(l, c):
    print(f'A área de um tereno {l:.2f}m x {c:.2f}m é de {l * c:.2f}m²')



print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
print('-' * 20)

area(l, c)

