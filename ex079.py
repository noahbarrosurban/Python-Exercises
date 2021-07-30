lista = []
res = ' '
num = int(input('Digite um valor: '))

while True:
    if num in lista:
        print('Valor duplicado! Não vou adicionar.')
    else:
        lista.append(num)
        print('Valor adicionado com sucesso!')

    res = input('Quer continuar? [S/N] ').strip().upper()[0]

    if res == 'S':
        num = int(input('Digite um valor: '))
    else:
        break

print(f'Você digitou os valores {sorted(lista)}')

#Ou

#num = list()

#while True:
    #n = int(input('Digite um valor: '))
    #if n not in num:
        #num.append(n)
        #print('Valor adicionado com sucesso!')
    #else:
        #print('Valor duplicado! Não vou adicionar.')

    #res = input('Quer continuar? [S/N] ').strip().upper()[0]
    #if res in 'N':
        #break
#print(f'Você digitou os valores {sorted(lista)}')
