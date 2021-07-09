frase = input('Digite uma frase: ').strip().upper()
separado = frase.split()
junto = ''.join(separado)
inverso = ''
for letra in range(len(frase)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')

