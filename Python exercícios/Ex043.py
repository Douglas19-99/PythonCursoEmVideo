peso = float(input('Qual seu peso em kg? '))
altura = float(input('Qual sua altura em metros? '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Com imc de {imc:.2f} você está abaixo do peso.')

elif imc > 18.5 and imc <= 25:
    print(f'Com imc de {imc:.2f} você está com o peso ideal.')
