'''from math import factorial
num = int(input('Digite um número para calcular seu Fatorial: '))
print(f'Calculando {num}! = {factorial(num)}')'''

num = int(input('Digite um número para calcular seu Fatorial: '))
cont = num
f = 1
print(f'Calculando {num}!')
while cont > 0:
    print(f'{cont}',end='')
    print(' x ' if cont > 1 else ' = ',end='')
    f *= cont
    cont -= 1
print(f'{f}')