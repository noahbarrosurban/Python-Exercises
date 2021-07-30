def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número válido.')
            continue
        except (KeyboardInterrupt):
            print('OUsuário preferiu não digitar esse número.')
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número válido.')
            continue
        except (KeyboardInterrupt):
            print('Eroo: O Usuário preferiu não digitar esse número.')
        else:
            return n


n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')

print(f'O valor Inteiro digitado foi {n1} e o Real foi {n2}')