from datetime import date

smaiores = 0
smenores = 0

a1 = date.today().year

for pessoas in range(1,8):
    a2 = int(input(f'Em que ano a {pessoas}ª pessoa nasceu? '))
    if a1 - a2 >= 21:
        smaiores += 1
    else:
        smenores += 1

print(f'Ao todo tivemos {smaiores} pessoas maiores de idade')
print(f'E tivemos {smenores} pessoas menores de idade')