# Un clousure es una función que define a otra, y además la regresa
# La función anidada puede acceder a las variable locales definidas en la función principal o externas

# Función principal closure utilizando lamda
def operacion(a, b):
  # 1. Definimos una función lambda interna o anidada
  return lambda: a + b
  
  
mi_funcion_closure_lambda = operacion(5,3)
print(f'Resultado de la función closure lambda: {mi_funcion_closure_lambda()}')

# Llamar al vuelo
print(f'Resultado de la función closure lambda al vuelo: {operacion(5,3)()}')
