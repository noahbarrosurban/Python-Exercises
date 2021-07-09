from random import randint
from time import sleep

items = ('Rock', 'Paper', 'Scissors')
computer = randint(0,2)

print("Let's play JO-KEN-PO?")

player1 = int(input('''Your options:
[ 0 ] ROCK
[ 1 ] PAPER
[ 2 ] SCISSORS
What's your move? '''))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')

print('-=' * 11)

print(f'Computer played {items[computer]}')
print(f'Player 1 played {items[player1]}')

print('-=' * 11)

if computer == 0:
    if player1 == 0:
        print('TIED')
    elif player1 == 1:
        print('PLAYER 1 WON!')
    elif player1 == 2:
        print('COMPUTER WON!')

elif computer == 1:
    if player1 == 0:
        print('COMPUTER WON!')
    elif player1 == 1:
        print('TIED')
    elif player1 == 2:
        print('PLAYER 1 WON!')

elif computer == 2:
    if player1 == 0:
        print('PLAYER 1 WON!')
    elif player1 == 1:
        print('COMPUTER WON!')
    elif player1 == 2:
        print('TIED')