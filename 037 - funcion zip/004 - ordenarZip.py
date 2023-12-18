

# Ordenando con zip

letras = ['c', 'd', 'a', 'e', 'b']
numeros = [3, 2, 4, 1, 0]

mezcla = zip(letras, numeros)

# Sin orden
print(tuple(mezcla))

# ordenar por letra (primer iterable)
print(sorted(zip(letras, numeros)))

# ordenar por numero(segundo iterable)
print(sorted(zip(numeros, letras)))
