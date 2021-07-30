from random import randint
soma = []

def maior(*num):
    nmaior = 0
    print('-=' * 20)
    print('Analisando os valores informados...')
    for i in range(0, randint(1, 11)):
        print(f'{i} ', end='')
        soma.append(i)
    print()
    print(f'Foram informados {len(soma)} valores ao todo.')
    for i in soma:
        if i > nmaior:
            nmaior = i
    print(f'O maior valor informado foi {nmaior}.')




maior()


'''def maior(*num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores informados...')
    for i in num:
        print(f'{i} ', end='')
        if i > maior:
            maior = i
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior vvalor informado foi {maior}')



maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)'''









