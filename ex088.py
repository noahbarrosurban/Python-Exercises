from random import randint
lista = list()
jogos = list()
quant = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1

while total <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    print(f'Jogo {total}: {sorted(lista)}')
    lista.clear()
    total += 1

