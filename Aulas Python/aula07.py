# print(5+2)
# print(5-2)
# print(5*2)
# print(5/2)
# print(5**2) # Potência
# print(5//2) # Divisão inteira
# print(5%2) # Resto da divisão/Módulo

'''
Ordem de precedência:

1 = ()
2 = **
3 = * / // %
4 = + -
'''
# nome = input('Qula seu nome? ')
# print('Prazer em te conhecer {:<>^20}!'.format(nome))
# Formatando a variavel dentro do print.

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {} o produto é {} e a divisão é {:.3f}'.format(s, m, d))
print('Divisão intiera {}  e a potência {:.1f}'.format(di, e))
