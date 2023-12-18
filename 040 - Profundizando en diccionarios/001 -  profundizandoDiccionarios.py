


# Los dic guardan un orden (a diferencia de un set)
diccionario = {'Nombre': 'Juan', 'Apeliido': 'Pérez', 'Edad':28}
print(diccionario)


# Los dic son mutables, pero las lalves deben ser inmutables
# diccionario = {[1, 2]:'Valor1'}
#diccionario = {(1,2):'Valor1'}
#print(diccionario)

# Se agrega la llave si no existe. Si ya existe, se actualiza
diccionario['Departamento'] = 'Sistemas'
print(diccionario)

# Actualizar (No hay valores duplicados en las llaves de un diccionario)
diccionario['Nombre'] = 'Juan Carlos'
print(diccionario)

# Recuperar un valor indicando una llave
print(diccionario['Nombre'])
# Si no encuentra la llave lanza una excepción
#print(diccionario['nombre'])

# Método get recupera una llave, y si no existe NO lanza excepción
# además podemos regresar un valor en caso de que no exista la llave

print(diccionario.get('Nombres', 'No se encontró la llave'))

nombre = diccionario.setdefault('Nombre', 'valor por default')
print(nombre)
print(diccionario)

# Imprimir con pprint
from pprint import pprint as pp
pp(diccionario, sort_dicts=False)