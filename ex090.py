dic = {'nome': input('Nome: '), 'media': float(input('Média: '))}

print(f'O nome é igual a {dic["nome"]}')
print(f'A média é igual a {dic["media"]}')

if dic['media'] >= 7:
    print(f'Situação é igual a Aprovado')
else:
    print(f'Situação é igual a Reprovado')
