'''
 Escreva um programa que leia a velocidade de um carro.
 Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
 A multa vai custar R$7,00 por cada Km acima do limite.
'''
vel_motorista = float(input('Qual é a velocidade atual do carro? km/h '))
vel_maxima = 80

if vel_motorista > 80:
    print(f'Você foi multado. A sua multa é de R${(vel_motorista - vel_maxima) * 7:.2f}')
print('Tenha um bom dia! Dirija com segurança.')
