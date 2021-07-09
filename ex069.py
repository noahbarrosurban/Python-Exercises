maiores = homens = mulheresmaiores = 0

while  True:
    print('-' * 45)

    print('''           CADASTRE UMA PESSOA''')

    print('-' * 45)

    idade = int(input('Idade: '))
    genero = ' '

    while genero not in 'MF':
        genero = input('Gênero: [M/F] ').strip().upper()[0]

    print('-' * 45)

    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Quer continuar? [S/N] ').strip().upper()[0]

    if idade >= 18:
        maiores += 1

    if genero == 'M':
        homens += 1

    elif genero == 'F':
        if idade <= 18:
            mulheresmaiores += 1

    if resposta == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheresmaiores} mulheres com menos de 20 anos')