'''
Faça um algortimo que leia o salário de um funcionário e
mostre seu novo salário, com 15% de aumento.
'''

salario = float(input('Qual seu salário? R$'))
valor_final = salario + (salario * 15 / 100)

print(f'Um funcionário que ganhava R${salario:.2f},\n'\
    f'com 15% de aumento, passou a receber R${valor_final:.2f}.')

