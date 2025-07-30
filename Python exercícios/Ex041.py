'''
A Confederação Nacional de Natação precisa de um programa
que leia o ano de nascimentode um atleta e mostre sua categoria, de acordo com a idade:
'''

from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nascimento

if idade <= 9:
    print(f'Com {idade}, você está na categoria MIRIM.')

elif idade > 9 and idade <= 14:
    print(f'Com {idade}, você está na categoria INFANTIL.')

elif idade > 14 and idade <= 19:
    print(f'Com  {idade}, você está na categoria JUNIOR.')

elif idade <= 25:
    print(f'Com {idade}, você está na categoria SÊNIOR.')

else:
    print(f'Com {idade}, você está na categoria MASTER.')