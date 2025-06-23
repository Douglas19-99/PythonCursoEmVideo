frase = str(input('Digite uma frase: ')).strip().upper()
# frase = 'Se está com medo, vai com medo mesmo.'
print(f'A letra A aparece {frase.count('A')} vezes na frase.')
print(f'A primeira posição que a letra A aparece é {frase.find('A')+1}')
print(f'A última posição que a letra A aparece é {frase.rfind('A')+1}')