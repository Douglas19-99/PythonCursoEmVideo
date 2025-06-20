'''
Faça um programa que leia a largura e a altura de uma parede
em metros, calcule a sua área e a quantidade de tinta necessária para
pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m². 
'''
entrada1 = float(input('Digite a largura da sua parede: '))
entrada2 = float(input('Digite a altura da sua parede: '))

area = entrada1 * entrada2
litros = area / 2

print(f'A área em m² de sua parede é {area}m²', end= '\n' 
      f'e a cada 2m² será necessária {litros} litros de tinta')