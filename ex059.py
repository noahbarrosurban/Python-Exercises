n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
calcular = 0

print('=-'*10)

while calcular < 5:
    calcular = int(input(
'''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
>>>>>>>>Qual é sua opção? '''))
    if calcular == 1:
        print(f' a soma entre {n1} e {n2} é igual a {n1 + n2}')
    elif calcular == 2:
        print(f' a multiplicação entre {n1} e {n2} é igual a {n1 * n2}')
    elif calcular == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior valor é {n1}')
        elif n1 == n2:
            print('Não existe número maior, eles são iguais')
        else:
            print(f'Entre {n1} e {n2} o maior valor é {n2}')
    elif calcular == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    print('=-' * 10)
print('Fim do programa! Volte sempre!')



