from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nascimento

if idade <= 9:
    print(f'Com {idade} você está na categoria MIRIM.')

elif idade > 9 and idade <= 14:
    print(f'Com {idade} você está na categoria INFANTIL.')

elif idade > 14 and idade <= 19:
    print(f'Com  {idade} você está na categoria JUNIOR.')

elif idade > 19 and idade <= 20:
    print(f'Com {idade} você está na categoria SÊNIOR.')

elif idade > 20:
    print(f'Com {idade} você está na categoria MASTER.')