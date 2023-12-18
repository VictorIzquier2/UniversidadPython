

# crear un diccionario con zip

llaves = ['Nombre', 'Apellido', 'Edad']
valores = ['Juan', 'Perez', 19]

diccionario = dict(zip(llaves, valores))

print(diccionario)

# Actualizar un elemento de un diccionario
llave = ['Edad']
nueva_edad = [28]
diccionario.update(zip(llave, nueva_edad))
print(diccionario)