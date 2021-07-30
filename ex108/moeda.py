def aumentar(p = 0, t = 0):
    res = p + (p * t / 100)
    return res

def diminuir(p = 0, t = 0):
    res = p - (p * t / 100)
    return res


def dobro(p = 0):
    res = p * 2
    return res


def metade(p = 0):
    res = p / 2
    return res


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda} {preço:.2f}'.replace('.', ',')