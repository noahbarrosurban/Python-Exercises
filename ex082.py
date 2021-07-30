lista = []
listapar = []
listaimpar = []

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)

    resp = input('Deseja continuar? [S/N] ')
    if resp in 'Nn':
        break

print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {listapar}')
print(f'A lista de impares é: {listaimpar}')