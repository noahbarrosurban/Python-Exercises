'''import random
nome = random.choice(Luiza, Noah, Zelia, Paulo)
print(f'O aluno escolhido foi o: {nome})'''

from radom import choice
n1 = input('Primeiro aluno: ')
n2 = input('Segndo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1,n2,n3,n4]
print(f'O aluno escolhido foi {choice(lista)}')