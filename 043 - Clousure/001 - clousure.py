# Un clousure es una función que define a otra, y además la regresa
# La función anidada puede acceder a las variable locales definidas en la función principal o externas

# Función principal
def operacion(a, b):
  # definimos una función interna o anidada
  def sumar(): # Función clousure
    return a + b
  
  # Retornar la función
  return sumar

mi_funcion_closure = operacion(5, 2)

print(f'Resultado de la función closure: {mi_funcion_closure()}')

# Llamar la función regresada al vueo
print(f'Resultado de la función closure al vuelo: {operacion(2, 3)()}')