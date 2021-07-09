cont = 1

while True:
    t = int(input('Quer ver a tabuada de qual valor? '))
    if t < 0:
        break

    print('-' * 50)

    for m in range(1,11):
        print(f'{t} x {m} = {t * m}')
        m += 1

    print('-' * 50)

