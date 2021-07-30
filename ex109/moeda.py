def aumentar(p = 0, t = 0, formato = False):
    res = p + (p * t / 100)
    return res if formato is False else moeda(res)

def diminuir(p = 0, t = 0, formato = False):
    res = p - (p * t / 100)
    return res if formato is False else moeda(res)


def dobro(p = 0, formato = False):
    res = p * 2
    return res if formato is False else moeda(res)


def metade(p = 0, formato = False):
    res = p / 2
    return res if formato is False else moeda(res)


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda} {preço:.2f}'.replace('.', ',')