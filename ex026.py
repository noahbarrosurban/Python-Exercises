f = input('Digite aqui sua frase: ').upper().strip()
print(f'A letra "A" aparece {f.count("A")} na frase')
print(f'A primeira letra "A" apareceu na posição {f.find("A")+1}')
print(f'A última letra "A" apareceu na posição {f.rfind("A")+1}')
