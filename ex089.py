aluno = []
sala = []
resp = 0
while True:
    aluno.append(input('Nome: '))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    aluno.append((aluno[1] + aluno[2]) / 2)
    sala.append(aluno[:])
    aluno.clear()

    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')

for i, a in enumerate(sala):
    print(f'{i:<4}{a[0]:<10}{a[3]:>8}')

while True:
    resp = int(input('Mostrar notas de qual aluno? [999 interrompe]'))
    if resp <= len(sala) - 1:
        print(f'Notas de {sala[resp][0]} são {sala[resp][1]} e {sala[resp][2]}')
    if resp == 999:
        break