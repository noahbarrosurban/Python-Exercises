v = float(input('Qual o valor do produto? '))
f = input('Qual a forma de pagamento? ').strip()
if f.upper() == 'CARTÃO' or f.upper() == 'CARTAO':
    c1 = int(input('Quantas vezes no cartão? '))
    if c1 == 1:
        print(f'Aplicando 5% de desconto, o valor do produto ficará R$ {v - ((v * 5) / 100):.2f}')
    elif c1 == 2:
        print(f'O valor do produto ficará R$ {v:.2f}')
    else:
        print(f'Aplicando 30% de juros, o valor do produto ficará R$ {v + ((v * 10) / 100):.2f}')
elif f.upper() == 'DINHEIRO' or f.upper() == 'CHEQUE':
    print(f'Aplicando 10% de desconto, o valor do produto ficará R$ {v - ((v * 10) / 100):.2f}')
else:
    print('Desistiu da compra, arrombado?')

