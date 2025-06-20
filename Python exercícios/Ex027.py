nome = input('Qual seu nome completo? ')
p_s = nome.split()

print(f'Nome digitado foi {nome}')
print(f'Primeiro nome: {p_s[0]}')
print(f'Segundo nome: {p_s[-1]}')
