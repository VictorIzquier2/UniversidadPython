# Funciones lambda
# Son funciones anónimas, y son pequeñas (una línea de código)

# Directanmente no se puede asignar una función a la declaración de una nueva variable
#mi_funcion = def sumar(a, b): 
#  return a + b

# Con una función lambda(La función es anónima y ocupa una sola línea de código)
# No se necesita agregar paréntesis para los parámetros
# No se necesita usar la palabra return, pero sí debe regresar una expresión válida

mi_funcion_lambda = lambda a, b : a + b

resultado = mi_funcion_lambda(4,6)
print(resultado)

# Función lambda que no recibe argumentos ( debemos regresar una expresión válida)
mi_funcion_lambda = lambda: 'Función sin argumentos'
print(f'Llamar función lambda sin argumentos: {mi_funcion_lambda()}')

# Función lambda con parámetros por default
mi_funcion_lambda = lambda a=2, b=3: a + b
print(f'Resultado argumentos por default: {mi_funcion_lambda()}')

# Función lambda con argumentos variables *args y ***args, **kwargs
mi_funcion_lambda = lambda *args, **kwargs: len(args) + len(kwargs)
print(f'Resultado argumentos variables: {mi_funcion_lambda(1,2,3, a=4, b=5, c=6)}')

# Funciones lambda con argumentos, argumentos variables y valores por default
mi_funcion_lambda = lambda a, b, c=3, *args, **kwargs: a+b+c+len(args)+len(kwargs)
print(f'resultado de la función lambda: {mi_funcion_lambda(1,2,4,5,6,7,z=8, y=9)}')