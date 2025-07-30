'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
de acordo com a tabela abaixo:
IMC abaixo de 18,5: Abaixo do Peso

Entre 18,5 e 25: Peso Ideal

25 até 30: Sobrepeso

30 até 40: Obesidade

Acima de 40: Obesidade Mórbida
'''

peso = float(input('Qual seu peso? (Kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Com imc de {imc:.2f}, você está ABAIXO DO PESO.')
    
elif imc > 18.5 and imc <= 25:
    print(f'Com imc de {imc:.2f}, você está com o PESO IDEAL.')

elif imc > 25 and imc <= 30:
    print(f'Com imc de {imc:.2f}, você está com SOBREPESO.')

elif imc > 30 and imc <= 40:
    print(f'Com imc de {imc:.2f}, você está com OBESIDADE.')

else:
    print('Você está com OBESIDADE MÓRBIDA.')    
