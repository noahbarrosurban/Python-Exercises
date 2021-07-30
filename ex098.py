from time import sleep
def contador(a, b, c):
    if c == 0:
        c = 1
    print('-=' * 20)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    for i in range(a,b,c):
        print(f'{i} ', end='')
        sleep(0.5)
    print('Fim!')



contador(1,10,1)

contador(10, 0, -2)

print('-=' * 20)
print(f'Agora é sua vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))

contador(a,b,c)