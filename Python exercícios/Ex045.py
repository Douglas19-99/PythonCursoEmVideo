import random
print('---JOKENPÕ---')
print('Escolha o que jogar:')
print('Pedra')
print('Papel')
print('Tesoura')
print('-' * 20)


jogador = str(input('Qual opção você escolhe? ')).lower()

nomes_sorteados = ['Pedra', 'Papel', 'Tesoura']
computador = random.choice(nomes_sorteados)


if jogador not in nomes_sorteados:
    print('Entrada incorreta, tente novamente.')

elif jogador == computador:
    print('Empate.')

elif (jogador == 'Papel' and computador == 'Pedra' or\
jogador == 'tesoura' and computador == 'Papel' or\
jogador == 'Pedra' and computador == 'Tesoura'):
    print('PARABÉNS! Você venceu!')


else:
    print('Você perdeu, Tente novamente.')

