'''
Crie um programa que leia quanto dinheiro uma pessoa tem
na carteira e mostre quantos Dólares ela poder comprar.
'''

reais = float(input('Diga quantos reais você tem na carteira: '))

dolar = reais / 5.55

print(f'Você pode comprar {dolar:.0f} Dólares com o dinheiro que tem na carteira.')

