from datetime import date
a1 = int(input('Qual seu ano de nascimento? '))
a2 = date.today().year
a3 = a2 - a1
if a3 < 18:
    print(f'Daqui a {18 - a3} anos você terá que se alistar no serviço militar!')
elif a3 == 18:
    print('Está na hora de se alistar no serviço militar!')
else:
    print(f'Você deveria ter se alistado há {a3 - 18} anos no serviço militar!')