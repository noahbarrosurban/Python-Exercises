v = float(input('Digite a velocidade do carro em Km/h: '))
if v > 80:
    print(f'Você foi multado! O valor da multa é de R${(v - 80) * 7:.2f}')
else:
    print('Muito bem! Dirija sempre comm atenção :D')
