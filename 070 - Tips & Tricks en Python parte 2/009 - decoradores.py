# Los decoradores permiten extender y modificar el comportamiento de las funciones
# Ejemplos comunes: logging, seguridad, caching

# Un decorador es codigo reutilizable
# Primer ejemplo de un decorador
def decorador_envolvente(funcion_a_decorar):
  # Recibir la función y regresarla
  print('Estamos dentro de la función decoradora')
  return funcion_a_decorar

# Ahora utilizamos el decorador
def saludar():
  return 'Saludos desde mi función saludar'

# Llamamos manualmente el decorador (No es lo común en Python)
funcion_retornada = decorador_envolvente(saludar())
print(funcion_retornada)

@decorador_envolvente
def saludar_funcion_a_decorar():
  return 'Saludos desde función a decorar...'

print(saludar_funcion_a_decorar())

# Decorador que convierte el texto a mayúsculas
def mayusculas(funcion_a_decorar):
  def envolvente():
    # Mandamos a llamar la función original (closure)
    resultado_original = funcion_a_decorar()
    resultado_modificado = resultado_original.upper()
    return resultado_modificado
  return envolvente

@mayusculas
def saludar_minusculas():
  return 'hola...'

print(saludar_minusculas())