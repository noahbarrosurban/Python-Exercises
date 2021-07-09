print('=' * 50)
print('''               BANK SIMULATOR''')
print('=' * 50)

value = int(input('What amount do you want to withdraw? $ '))
total = value
bn = 50
totalbn = 0

while True:
    if total >= bn:
        total -= bn
        totalbn += 1

    else:
        if totalbn > 0:
            print('=' * 50)
            print(f'''              {totalbn} ${bn} bills total''')
        if bn == 50:
            bn = 20
        elif bn == 20:
            bn = 10
        elif bn == 10:
            bn = 1

        totalbn = 0

        if total == 0:
            break

print('=' * 50)
print('Always come back to the BANK SIMULATOR!')