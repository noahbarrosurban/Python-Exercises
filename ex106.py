def ajuda(com):
    help(com)

def título(msg, cor=0):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)



comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP')
    comando = input('Função ou Biblioteca > ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('Até logo!')