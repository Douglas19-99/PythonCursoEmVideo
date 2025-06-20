from math import hypot

cat_oposto = float(input('Digite o cateto oposto: '))
cat_adjacente = float(input('Digite o cateto adjacente: '))

# hipotenusa = sqrt(cat_oposto**2 + cat_adjacente**2)
hipotenusa = hypot(cat_oposto, cat_adjacente)

print(f'A comprimento da hipotenusa: {hipotenusa:.2f}')
