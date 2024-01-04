# Las funciones en python son ciudadanos de primera clase
def mayusculas(texto):
  return texto.upper()

# Uso normal de una funcion
print(mayusculas('Hola'))

# Uso de una función como un objeto
# Asignar la referencia de la función a una variable, sin los paretesis
variable_funcion = mayusculas

# Apuntan las dos a la misma referencia en memoria
print(mayusculas)
print(variable_funcion)

# Utilizamos la variable función en cualquier momento
print(variable_funcion('Nuevo Texto'))

# Para demostrar que las funciones son objetos, eliminamos la referencia original
del mayusculas

# Aún así, podemos utilizar la función con la variable_funcion
print(variable_funcion('Saludos...'))
# print(mayusculas('Ya se eliminó')) Da error

# Podemos saber el nombre por default que se le asigna a una funcion
print(f'Nombre por default de la función: {variable_funcion.__name__}')






