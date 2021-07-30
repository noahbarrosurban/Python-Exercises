def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'Erro! {entrada} é um preço invválido!')
        else:
            válido = True
            return float(entrada)