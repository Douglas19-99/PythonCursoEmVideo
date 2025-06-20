from math import radians, sin, cos, tan

angulo_graus = float(input('Digite o angulo em graus: '))

angulo_radiano = radians(angulo_graus)

seno = sin(angulo_radiano)
cosseno = cos(angulo_radiano)
tangente = tan(angulo_radiano)

print(f'O seno de {angulo_graus}° = {seno:.2f}')
print(f'O cosseno de {angulo_graus}° = {cosseno:.2f}')
print(f'A tangente de {angulo_graus}° = {tangente:.2f}')

