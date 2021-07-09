print('=-' * 25)
print("Let's play ODDS OR EVENS!")
print('=-' * 25)

conttot = 0
contwon = 0

while True:
    from random import randint
    from time import sleep

    computervalue = randint(0, 10)
    player1value = int(input('Enter a value: '))
    player1oddsorevens = input('Odds or evens? [O/E] ').strip().upper()[0]
    add = computervalue + player1value
    addoddsorevens = ''

    while player1oddsorevens not in 'EO':
        player1oddsorevens = input('Odds or evens? [O/E] ').strip().upper()[0]

    if add % 2 == 0:
        addoddsorevens = 'EVEN'
    else:
        addoddsorevens = 'ODD'

    print('=-' * 25)

    print('Once')
    sleep(0.5)
    print('Twice')
    sleep(0.5)
    print('Three')
    sleep(0.5)
    print('SHOOT!')
    sleep(0.5)

    print('=-' * 25)

    print(f'You played {player1value} and the computer {computervalue}! The total sum is {player1value + computervalue}, {addoddsorevens}!')

    if player1oddsorevens == 'E':
        conttot += 1
        if add % 2 == 0:
            contwon += 1
            print('PLAYER 1 WON!')
        else:
            break
    else:
        conttot += 1
        if add % 2 == 0:
            break
        else:
            contwon += 1
            print('PLAYER 1 WON!')

    print("Let's play again!")
    print('=-' * 25)

print('COMPUTER WON!')
print(f'GAME OVER! You played {conttot} times and won {contwon}.')





