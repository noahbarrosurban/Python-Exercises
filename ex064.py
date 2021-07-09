num = cont = soma = 0

while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        soma += num
        cont += 1
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')

