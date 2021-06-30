print('O computador está gerando um número...')
from random import randint
n1 = randint(0,5)
n2 = int(input('Qual você acha que foi o número gerado? '))
if n1 == n2:
    print(f'Parabéns, você acertou! O número era {n1} ')
else:
    print(f'Você errou! O número era {n1} ')
