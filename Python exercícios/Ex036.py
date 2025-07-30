'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''
# Solicitei os valores.
Valor_casa = float(input('Qual o valor da casa: R$'))
Salario = float(input('Qual do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))

# Fiz os calculos de porcetagem e prestação.
prestação = Valor_casa / (anos * 12)
porcentagem = Salario * (30/100)

if prestação <= porcentagem:
    print(f'Para pagar um casa de R${Valor_casa} em {anos}')
    print(f'a prestação será de R${prestação:.2f}')
    print('Empréstimo pode ser CONCEDIDO!')

else:
    print(f'Empréstimo não concedido.')
 


