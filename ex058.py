from random import randint
computer = randint(0,10)
print('Sou seu computador! Acabei de pensar em um número entre 0 e 10. Você consegue adivinhar qual foi? ')
pessoa = int(input('Qual é seu palpite? '))
palpite = 1
while pessoa != computer:
    if pessoa > computer:
        print('Menos... Tente mais uma vez. ')
        pessoa = int(input('Qual é seu palpite? '))
    if pessoa < computer:
        print('Mais... Tente mais uma vez. ')
        pessoa = int(input('Qual é seu palpite? '))
    palpite += 1
print(f'Acertou com {palpite} tentativa. Parabéns')