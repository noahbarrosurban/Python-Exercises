expressao = input('Digite uma expressão: ')
lista = []

for simbolo in expressao:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop() #pop exclui o último elemento da lista
        else:
            lista.append(')')
if len(lista) == 0:
    print('Sua expressão é valida!')
else:
    print('Sua expressão não é valida!')