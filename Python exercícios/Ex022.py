nome = input('Qual é seu nome? ')
nome_sem_espaços = nome.replace(' ', '')
primeiro_nome = nome.split()[0]

print('Seu nome em maiúsculo:', nome.upper())
print('Seu nome em minúsculo:', nome.lower())
print(f'Seu nome tem {len(nome_sem_espaços)} letras sem considerar os espaços.')
print(f'Seu primeiro nome tem {len(primeiro_nome)} letras.')