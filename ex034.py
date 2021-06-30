s = float(input('Digite o valor do salário em reais: '))
if s > 1250:
    print(f'O valor final será R$ {s + ((s * 10)/100):.2f}')
else:
    print(f'O valor final será R$ {s + ((s * 15) / 100):.2f}')