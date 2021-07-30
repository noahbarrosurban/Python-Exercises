from datetime import date

atual = date.today().year
dados = {}

dados['nome'] = (input('Nome: '))
dados['idade'] =  atual - int(input('Ano de Nascimento: '))
dados['ctps'] = int(input('Carteira de trabalho [0 não tem]: '))

if dados['ctps'] > 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = int(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + (35 - (atual - dados['contratação']))

print(dados)
for k, v in dados.items():
    print(f'A {k} tem o valor {v}')