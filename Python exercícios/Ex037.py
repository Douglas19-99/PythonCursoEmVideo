from random import randint
from time import sleep

print('Calculadora de conversão')
print('-' * 20)
print('Nossas opções de conversão.')
print('1 para binário.')
print('2 para octal.')
print('3 para hexadecimal.')
print('-' * 20)

num = int(input('Digite o número que deseja converter: '))
opções = int(input('Escolha uma opção: '))
print('Processando...')
sleep(3)
binario = bin(num)[2:]      # Remove o prefixo '0b'
octal = oct(num)[2:]        # Remove o prefixo '0o'
hexadecimal = hex(num)[2:]  # Remove o prefixo '0x'

if opções == 1:
    print(f'{num} convertido para binário é {binario}.')

elif opções == 2:
    print(f'{num} convertido para octal é {octal}.')

elif opções == 3:
    print(f'{num} convetido para hexadecimal é {hexadecimal.upper()}.')

print('Obrigado por usar nossa calculador!')