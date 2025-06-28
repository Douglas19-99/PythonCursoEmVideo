'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''

km = float(input('Quantos Km você vai rodar na sua viagem? Km '))
if km <= 200:
    print(f'Você não ultrapassou o limite de 200 km então deverá pagar {km * 0.50:.2f}')
else:
    print(f'Você ultrapassou o limite de 200 km e deverá pagar {km * 0.45:.2f}')