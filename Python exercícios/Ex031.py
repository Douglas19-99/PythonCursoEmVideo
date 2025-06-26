km = float(input('Quantos Km você vai rodar na sua viagem? Km '))
if km < 200:
    print(f'Você não ultrapassou o limite de 200 km então deverá pagar {km * 0.50:.2f}')
else:
    print(f'Você ultrapassou o limite de 200 km e deverá pagar {km * 0.45:.2f}')