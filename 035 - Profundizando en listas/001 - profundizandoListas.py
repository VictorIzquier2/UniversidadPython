# Profundizando en listas
# Listas son mutables

nombres1 = ['Juan', 'Pedro', 'Pablo']
nombres2 = 'Laura María Gonzalo'.split()

suma = nombres1 + nombres2
print(suma)

# Extender una lista con otra lista
nombres1.extend(nombres2)
print(f'Extender la lista 1 con la lista 2: {nombres1}')

# lista de números
numeros1 = [10,40, 15, 4, 20, 90, 4]
print(f'Lista original: {numeros1}')

print(f'Indice 4: {numeros1.index(4)}')

numeros1.reverse()
print(numeros1)

numeros1.sort()
print(numeros1)

numeros1.sort(reverse=True)
print(numeros1)

print(f'valor mínimo: {min(numeros1)}')
print(f'valor máximo: {max(numeros1)}')

