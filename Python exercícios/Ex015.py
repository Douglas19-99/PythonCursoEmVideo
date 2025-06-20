km = float(input('Quantos Kms você rodou? '))
dias = int(input('Quantas diárias foram usadas? '))

TK = km * 0.15
TD = dias * 60
TT = TK + TD
# Formula mais direta = (dias * 60) + (km * 0.15)
print(f'Como você rodou {km} Km em {dias} Dias, você devera pagar R$ {TT:.2f}.')