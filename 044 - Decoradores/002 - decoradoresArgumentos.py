# decoradores con argumentos

def funcion_decorador_a(funcion_a_decorar_b):
  def funcion_decorada_c(*args, **kwargs):
    print('Antes desde la funcion_decorada_c')
    resultado = funcion_a_decorar_b(*args, **kwargs)
    print('Después desde la función decorada_c')
    return resultado
    
  return funcion_decorada_c

# Definimos una función y vamos a extender su funcionalidad con un decorador
@funcion_decorador_a
def sumar(a, b):
  return a + b

resultado = sumar(5, 6)
print(f'resultado suma: {resultado}')