'''
Escreva um programa que leia dois números inteiros e compare-os.
mostrando na tela uma mensagem
'''

print('Comparando números')
print('-' * 20)

num1 = int(input('Primeiro número? '))
num2 = int(input('Segundo número? '))

if num1 > num2:
    print('O PRIMEIRO número é maior.')

elif num1 < num2:
    print('O SEGUNDO número é maior.')

else:
    print('Os dois números são iguais.')
    