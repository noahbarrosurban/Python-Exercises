jogosps1 = ('Castlevania: Symphony of the Night', 'Chrono Cross', 'Crash Bandicoot', 'Crash Team Racing', 'Crash Team Racing',
            'Final Fantasy VII', 'Gran Turismo', 'Legacy of Kain: Soul Reaver', 'Legend of Dragoon', 'Medal of Honor',
            'Mega Man X4', 'Metal Gear Solid')
for i in jogosps1:
    print(f'\nNo jogo {i.upper()} temos ', end='')
    for l in i:
        if l.lower() in 'aeiou':
            print(l.lower(), end=' ')