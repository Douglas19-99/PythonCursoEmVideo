print('CALCULADORA DE MÉDIA')
print('-' * 20)
print()

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = nota1 + nota2 / 2

if média < 5.0:
    print(f'Com média {média} você está reprovado.')

elif média >= 5.0 and média <= 6.9:
    print(f'Com média {média} você está de recuperação.')

elif média >= 7.0:
    print(f'Sua média foi {média}')
    print('Parabéns! Você está aprovado.')

print('Obrigado, por ultilizar nossa ferramenta!')
