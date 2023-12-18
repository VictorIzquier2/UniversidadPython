# Profundizando set
# Un set es una colección de elementos únicos y es mutable
# los elementos de un set deben ser inmutables

#conjunto = {[1,2], [3,4]}
conjunto = {'Juan', True, 18.0}
print(conjunto)

# set vacío
conjunto = {}
print(type(conjunto))

# set vacío correcto
conjunto = set()
print(conjunto)
print(type(conjunto))

# Mutable
conjunto.add('Juan')
print(conjunto)

# Contiene valores únicos
conjunto.add('Juan')

# Crear un set a partir de un iterable
conjunto = set([4,5,7,8,4])
print(conjunto)

# Podemos agregar más elementos on incluso otro set
conjunto2 = {100, 200, 300, 400}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20,30,40,40])
print(conjunto)

# Copiar un set (copia poco profunda, solo copia referencias)
conjunto_copia = conjunto.copy()
print(conjunto_copia)

print(f'Es igual en contenido?: {conjunto == conjunto_copia}')
print(f'Es igual en contenido?: {conjunto is conjunto_copia}')

