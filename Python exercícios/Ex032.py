'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''
from datetime import date # Import o ano atual da máquina.
ano = int(input('Digite um ano qualquer: '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'{ano} é um ano BISSEXTO.')

else:
    print(f'{ano} não é um ano BISSEXTO.')
