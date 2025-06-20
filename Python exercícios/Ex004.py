entrada = (input('Digite algo: '))

print('O tipo primitivo desse valor é', type(entrada))
print('Tem espaços?', entrada.isspace())
print('É um número?', entrada.isdigit())
print('É alfabético?', entrada.isalpha())
print('É alfanúmerico', entrada.isalnum())
print('Está em maiúsculas?', entrada.isupper())
print('Está em minúscula?', entrada.islower())
print('Está capitalizada?', entrada.istitle())

# Treinei métodos neste exercício.