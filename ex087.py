matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = ter = maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if c == 2:
            ter += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maior:
                maior = matriz[l][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'A soma dos valores pares é: {par}')
print(f'A soma dos valores da terceira coluna é: {ter}')
print(f'O maior valor da segunda linha é: {maior}')