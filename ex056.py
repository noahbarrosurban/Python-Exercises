somaidade = 0
maioridadehomem = 0
nomevelho = 0
totalmulher20 = 0

for pessoa in range(1,5):
    print(f'--------- {pessoa}ª PESSOA ---------')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    genero = input('Genero [M/F]: ').strip().upper()
    somaidade += idade

    if pessoa == 1 and genero == 'M':
        maioridadehomem = idade
        nomevelho = nome

    if genero == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if genero == 'F' and idade < 20:
        totalmulher20 += 1

print(f'A média da idade do grupo é de {somaidade / 4:.0f} anos;')
print(f'O homem mais velho tem {maioridadehomem} e seu nome é "{nomevelho.capitalize()}".')
print(f'Ao todo são {totalmulher20} mulheres com menos de 20 anos.')

