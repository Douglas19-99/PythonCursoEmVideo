'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

à vista dinheiro/cheque: 10% de desconto

à vista no cartão: 5% de desconto

em até 2x no cartão: preço formal 

3x ou mais no cartão: 20% de juros
'''
print(f'{"CALCULADORA DE DESCONTO":=^40}') # ^ centraliza o texto, = 40 de casa lado.
print('-' * 20)
print('[1] - Dinheiro/Cheque.')
print('[2] - Cartão a vista.')
print('[3] - 2x no Cartão.')
print('[4] - 3x no Cartão.')
# Tentar otmizar esse programa.
preco = float(input('Qual o valor do produto? R$ '))
pagamento = int(input('Escolha a forma de pagamento: '))

dc = preco - (preco * 10/100)
cartao = preco - (preco * 5/100)
cartao3 = preco + (preco * 20/100)

if pagamento == 1:
    print(f'O valor original do produto é R${preco:.2f}, com o desconto de 10%,\n\
fica R${dc} por ter pago no dinheiro/cartão.')

elif pagamento == 2:
    print(f'O valor original do produto é R${preco:.2f}, com desconto de 5%,\n\
fica R${cartao:.2f} por ter pago à vista no cartão.')

elif pagamento == 3:
    print(f'Em 2x no cartão o valor do produto na muda.')

elif pagamento == 4:
    print(f'O valor do produto é R${preco:.2f}, com acréscimo de 20% de juros,\n\
por pagar em 3x no cartão o valor do produto sobe para R${cartao3:.2f}')

