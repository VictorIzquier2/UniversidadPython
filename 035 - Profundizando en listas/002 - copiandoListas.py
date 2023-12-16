

numeros1 = [10,40, 15, 4, 20, 90, 4]
print(f'Lista original: {numeros1}')

numeros2 = numeros1.copy()
print(f'Lista copiada: {numeros2}')

print(f'Misma referencia? {numeros1 is numeros2}')
print(f'Mismo contenido? {numeros1 == numeros2}')

# Constructor lista para copiar
numeros2 = list(numeros1)
print(f'Misma referencia? {numeros1 is numeros2}')
print(f'Mismo contenido? {numeros1 == numeros2}')

# slicing
numeros2 = numeros1[:]
print(f'Misma referencia? {numeros1 is numeros2}')
print(f'Mismo contenido? {numeros1 == numeros2}')

