'''
Desenvolva um programa que leia o comprimento de três retas e
diga ao usuário se elas podem ou não formar um triângulo e mostre o tipo de 
triângulo que será formado.
'''
print('-='*20)
print('Analizador de Triângulos')
print('-='*20)
r1 = float(input('Digite o tamanho da primeira reta: '))
r2 = float(input('Digite o tamanho da segunda reta: '))
r3 = float(input('Digite o tamanho da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os três segmentos podem sim formar um triângulo.')

else:
    print('Os três segmentos não podem formar um triângulo.')