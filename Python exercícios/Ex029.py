vel_motorista = float(input('Qual era a sua velocidade? km/h '))
vel_maxima = 80

if vel_motorista > 80:
    print(f'Você foi multado. A sua multa é de {(vel_motorista - vel_maxima) * 7}')

else:
    print('Você não foi multado.')