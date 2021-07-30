import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade do R${p} é R${moeda.metade(p)}')
print(f'O dobro do R${p} é R${moeda.dobro(p)}')
print(f'Aumentando 10% de R${p}, temos R${moeda.aumentar(p, 10)}')
print(f'Diminuindo 10% de R${p}, temos R${moeda.diminuir(p,10)}')