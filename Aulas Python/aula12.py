'''
Como criar estruturas condicionais aninhadas,
usando os comandos if, elif, else em programas Python.
'''
# Estrutura condicional aninhada.

nome = str(input('Qual é seu nome? '))

if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem normal')
print(f'Tenha um bom dia, {nome}')