sal = float(input('Qual seu salário? R$'))

if sal >= 1.250:
    print(f'Seu salário atual é {sal},\ncom o aumento de 10%, subiu para {sal + (sal*10/100)}')

else:
    print(f'Seu salário atual é {sal},\ncom o aumento de 15%, subiu para {sal + (sal*15/100)}') 