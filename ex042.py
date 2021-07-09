r1 = int(input('Digite o comprimento da primeira reta: '))
r2 = int(input('Digite o comprimento da segunda reta: '))
r3 = int(input('Digite o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas PODEM formar um triângulo:')
    if r1 == r2 == r3:
        print('Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r1:
        print('Isóceles')
    else:
        print('Escaleno')
else:
    print('Essas retas NÃO PODEM formar um triângulo!')