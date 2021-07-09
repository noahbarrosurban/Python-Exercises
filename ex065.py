continua = 'S'
contador = soma = media = maior = menor = 0

while continua == 'S':
    num = int(input('Digite um número: '))
    contador += 1
    soma += num

    if contador == 1:
        maior = menor = num

    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    continua = input('Deseja continuar? [S/N] ').strip().upper()[0]

media = soma / contador

print(f'Você digitou {contador} número e a média dos valores foi {media}')
print(f'O maior valor digitado foi {maior} e o menor valor foi {menor}')




