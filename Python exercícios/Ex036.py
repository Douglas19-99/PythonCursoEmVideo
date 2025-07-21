'''
'''
Valor_casa = float(input('Qual o valor da casa que deseja financiar? '))
Salario = float(input('Qual seu salário? '))
anos = int(input('Em quantos anos você vai pagar? '))

parcelas = anos * 12
prestação = Valor_casa//anos
porcentagem = (30 / 100) * Salario

if prestação < porcentagem:
    print(f'Empréstimo aprovado! Você ira pagar {parcelas} parcelas de R${prestação:.2f}.')
    print('Parabéns!!')
elif prestação > porcentagem:
     print(f'Empréstimo negado. Valor das parcelas é de R$ {parcelas},\n\
exedendo 30% do seu salário que é de R$ {Salario}.')
     print('Tente um valor menor na próxima consulta.')
print('Obrigado por escolher nosso Banco!')




