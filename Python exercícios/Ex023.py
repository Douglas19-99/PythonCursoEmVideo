num = int(input('Digite um número de 0 a 9999: '))
uni = num % 10
dez = num // 10 % 10
cent = num // 100 % 10
milhar = num // 1000 % 10

print(f'numero digitado: {num}')

print('Unidade:',uni)
print('Dezena',dez)
print('Centena:',cent)
print('Milhar:',milhar)
