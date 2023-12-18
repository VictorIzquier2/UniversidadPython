# Funciones anidadas

def calculadora(a, b, operacion='sumar'):
  # Función anidada
  def sumar(a, b):
    return a + b
  
  def restar(a, b):
    return a - b
  
  # LLamar a la función anidada
  if operacion == 'sumar':
    print(f'Resultado sumar: {sumar(a,b)}')
  elif operacion == 'restar':
    print(f'Resultado restar: {restar(a,b)}')
  
  
calculadora(5,6)
calculadora(7,3, operacion='restar')