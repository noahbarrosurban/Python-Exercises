v = float(input('Qual é o valor da casa? '))
s = float(input('Qual o salário do comprador? '))
a = int(input('Em quantos anos ele vai finalizar a compra? '))
m = (v/a)/12
if m > (s*30)/100:
    print('O empréstimo foi negado!')
else:
    print(f'O valor da prestação ficou R$ {m:.2f}')