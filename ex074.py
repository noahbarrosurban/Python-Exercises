'''from random import randint
cont = num = maior = menor = 0
tupla = ' '

while 0 <= cont <= 5:
    num = randint(0, 5)
    tupla += f'{num} '
    cont += 1

    if cont == 1:
        maior == menor == num

    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f'Os números sorteados foram:{tupla}')
print(f'O maior valor sorteado foi: {maior}')
print(f'O menor valor sorteado foi: {menor}')'''

from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')


