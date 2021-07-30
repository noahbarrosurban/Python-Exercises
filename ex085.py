lista = [[], []]
valor = 0

for i in range(1,8):
    valor = int(input(f'Digite o {i}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

print(f'Os valores pares digitados foram {sorted(lista[0])}')
print(f'Os valores impares digitados foram {sorted(lista[1])}')