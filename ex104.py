def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro! Digite um número inteiro válido.')
        if ok:
            break
    return valor




num = leiaInt('Digite um número: ')
print(f'Você acabopu de digitar o número {num}')
