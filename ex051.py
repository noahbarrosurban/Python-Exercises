a1 = int(input('Digite o priemiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
an = 0
for n in range (1,11):
    an = a1 + (n-1)*r
    print(an)
print('...')