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


def resumo(preço = 0, taxaa = 10, taxab = 5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Peço analisado: {moeda(preço)}')
    print(f'Dobro do preço: {dobro(preço, True)}')
    print(f'Metade do preço: {metade(preço, True)}')
    print(f'Com {taxaa}% de aumento: {aumentar(preço, taxaa, True)}')
    print(f'Com {taxab}% de redução: {aumentar(preço, taxab, True)}')
    print('-' * 30)