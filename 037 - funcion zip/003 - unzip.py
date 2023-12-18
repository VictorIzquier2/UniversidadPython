

# unzip con unpacking
mezcla = [(1,'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numeros, letras = zip(*mezcla)

print(f'Numeros: {numeros}, Letras: {letras}')
