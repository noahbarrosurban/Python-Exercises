
n = int(input('Digite um número inteiro: '))
c = int(input('''Escolha uma das bases para conversão:
1 - para binário 
2 - para octal
3 - para hexadecimal '''))
if c == 1:
    print(f'{bin(n)}'[2:])
elif c == 2:
    print(f'{oct(n)}'[2:])
elif c == 3:
    print(f'{hex(n)}'[2:])
else:
    print('INVÁLIDO')
