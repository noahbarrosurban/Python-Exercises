genero = input('Informe seu genero: [M/F] ').strip().upper()[0]
while genero not in 'FM':
    genero = input('Dados inválidos. Por favor, informe seu genero: [M/F] ').strip().upper()[0]
print(f'Genero {genero} registrado com sucesso')