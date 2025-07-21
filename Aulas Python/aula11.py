'''
vamos aprender como utilizar os códigos de escape sequence ANSI
para configurar cores para os seus programas em Python.
Veja como utilizar o código \033[m com todas as suas principais possibilidades.
'''
#\033[0;33;44m
# Style = 0: None / 1: Bold / 4: Underline / 7: Negative
# text = 30: Branco / 31: Vermelho / 32: Verde / 33: Amarelo / 34: Azul / 35: Roxo / 36: Azul claro / 37: Cinza
# Back = 40: Branco / 41: Vermelho / 42: Verde / 43: Amarelo / 44: Azul / 45: Roxo / 46: Azul claro / 47: Cinza

# print('\033[0;30;41m Texto teste \033[m')
# print('\033[4;33;44m Texto teste \033[m')
# print('\033[m texto teste \033[m')
# print('\033[7;30m texto teste \033[m')

# nome = 'Douglas'
# cores = {'limpa':'\033[m',
#           'azul':'\033[m',
#           'amarelo':'\033[m',
#           'pretoebranco':'\033[7;30m'}
# print(f'{cores["pretoebranco"]}{nome}{cores["limpa"]}')

