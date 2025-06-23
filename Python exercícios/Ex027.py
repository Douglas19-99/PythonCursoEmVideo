nome = input('Qual seu nome completo? ').strip()
print(f'Nome digitado foi {nome}')
print(f'Primeiro nome {nome.split()[0]}')
print(f'Segundo nome {nome.split()[-1]}')
