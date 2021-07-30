def escreva(txt):
    print('~' * len(txt))
    print(txt)
    print('~' * len(txt))


while True:
    txt = input('Digite um texto: ')
    escreva(txt)

    resp = input('Quer continuar? ')
    if resp in 'Nn':
        break
