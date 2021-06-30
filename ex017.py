from math import sqrt, trunc
'''o = float(input('Digite o valor do cateto oposto: '))
a = float(input('Digite o valor do cateto adjacente: '))
print(f'A hipotenusa desse triangulo é igual a {trunc(sqrt(o**2+a**2))}')'''

import math
o = float(input('Digite o valor do cateto oposto: '))
a = float(input('Digite o valor do cateto adjacente: '))
print(f'A hipotenusa desse triangulo é igual a {math.hypot(o,a):.2f}')



