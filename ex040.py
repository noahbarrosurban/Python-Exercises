n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
if (n1 + n2) / 2 < 5:
    print('REPROVADO')
elif 7 > (n1 + n2) / 2 >= 5:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')