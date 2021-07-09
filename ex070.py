preçototal = caro = menor = cont = 0
barato = ''

print('-' * 45)
print('''               NOAH'S STORE''')
print('-' * 45)

while True:
    produto = input('Nome do Produto: ').strip()
    preço = float(input('Preço: R$ '))
    preçototal += preço
    cont += 1
    resposta = ' '

    if preço > 1000:
        caro += 1

    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto

    while resposta not in 'SN':
        resposta = input('Quer continuar? [S/N] ').strip().upper()[0]

    if resposta == 'N':
        break

print('-' * 14, 'FIM DO PROGRAMA', '-' * 14)

print(f'O valor total da compra foi de R$ {preçototal:.2f}')
print(f'Temos {caro} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')