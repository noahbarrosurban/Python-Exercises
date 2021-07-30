cont9 = 0

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
n4 = int(input('Digite o último número: '))

num = (n1, n2, n3, n4)

print(f'Você digitou os valores: {num}')

if 9 in num:
    cont9 =+ 1
print(f'O valor 9 apareceu {cont9} vezes')

print(f'O valor 3 apareceu na {num.index(3)+ 1}ª posição')

print(f'Os números pares digitados foram: ', end='')

for n in num:
       if n % 2 == 0:
              print(n, end=' ')

'''num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite o último número: ')))

print(f'Você digitou os valores: {num}')

print(f'O valor 9 apareceu {num.count(9)} vezes')

if 3 in num:
       print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição')
else:
       print('O valor 3 não foi digitado em nenhuma posição')

print(f'Os números pares digitados foram: ', end='')

for n in num:
       if n % 2 == 0:
              print(n, end=' ')'''

