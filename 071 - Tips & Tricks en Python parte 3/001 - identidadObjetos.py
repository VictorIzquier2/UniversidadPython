# Identidad de objetos
# comparación del uso de operador == o el operador is en POO

# El operador == compara el contenido de 2 objetos (contenido igual)
# no necesariamente son el mismo objeto (pueden apuntar a objetos en memoria distintos)

# Operador is revisa si dos objetos son iguales (objetos idénticos)
# Ambos deben estar apuntando a la misma dirección de memoria para ser iguales

# Ejemplo de una lista
lista_a = [1,2,3]
lista_b = lista_a

print(f' Lista a y b tienen el mismo contenido?: {lista_a == lista_b}')
print(f' Lista a y b apuntan al mismo objeto?: {lista_a is lista_b}')


# Sin embargo, si creamos un nuevo objeto
lista_c = list(lista_a)

print(f' Lista a y c tienen el mismo contenido?: {lista_a == lista_c}')
print(f' Lista a y c apuntan al mismo objeto?: {lista_a is lista_c}')




