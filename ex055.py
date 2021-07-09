maior = 0
menor = 0

for pessoa in range(1,7):
    peso = float(input(f'O peso da {pessoa}ª pessoa: '))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')




