from datetime import date
a1 = int(input('Digite seu ano de nascimento: '))
a2 = date.today().year
a3 = a2 - a1
if a3 <= 9:
    print('MIRIM')
elif a3 <= 14:
    print('INFANTIL')
elif a3 <= 19:
    print('JUNIOR')
elif a3 <= 20:
    print('SÊNIOR')
else:
    print('MASTER')