from random import randint

def sorteia(lista):
    print(f'Sorteando 5 valores... ', end='')
    for i in range(0, 5):
        lista.append(randint(0,10))
    print(lista)

def somaPar(lista):
    print(f'Somando os valores pares de {lista}, temos ', end='')
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(soma)


lista = []
sorteia(lista)
somaPar(lista)