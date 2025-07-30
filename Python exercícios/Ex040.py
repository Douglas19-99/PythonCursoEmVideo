'''
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

Média abaixo de 5.0: REPROVADO
Média entre 5.0 e 6.9: RECUPERAÇÃO
Média 7.0 ou superior: APROVADO
'''

print('CALCULADORA DE MÉDIA')
print('-' * 20)
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2}, a média do aluno(a) é {média:.1f}')

if média < 5.0:
    print(f'Com média {média} você está reprovado.')

elif média >= 5.0 and média <= 6.9:
    print(f'Com média {média:.1f} você está em recuperação.')

elif média >= 7.0:
    print(f'Sua média foi {média:.1f}')
    print('Parabéns! Você está aprovado.')

print('Obrigado, por ultilizar nossa ferramenta!')
