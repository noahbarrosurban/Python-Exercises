lista = []

for i in range (0,5):
    num = int(input(f'Digite um valor: '))

    if i == 0:
        lista.append(num)
        print('Valor adicionado à lista')
    elif num > lista[-1]:
         lista.append(num)
         print('Valor adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Valor adicionado na posição {pos + 1} da lista')
                break
            pos += 1

print(f'Os valores digitados em ordem foram {lista}')
