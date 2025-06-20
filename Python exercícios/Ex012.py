'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
com 5% de desconto.
'''

valor = float(input('Qual o preço desse produto? R$'))
valor_final = valor - (valor * 5 / 100)

print(f'O valor liquido com desconto é R${valor_final}.')

