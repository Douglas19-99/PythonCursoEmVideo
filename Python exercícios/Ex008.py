'''
Escreva um programa que leia um valor em metros e o exiba convertido
em centímetros e milímetros.
'''
entrada = float(input('Digite um valor em metros: '))
cm = entrada * 100
mm = entrada * 1000

print(f'Seu valor em cm é {cm}  e em milimetros é {mm}')