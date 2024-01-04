#################################################################
# Closures
# Las funciones internas pueden capturar y guardar el estado de la función externa

from typing import Any


def hablar(texto, volumen):
  # La función interna ya no recibe parámetros
  # Utiliza el estado de la función padre (externa)
  def minusculas():
    return texto.lower()
  
  def mayusculas():
    return texto.upper()
  
  if volumen > 0.5:
    return mayusculas()
  else:
    return minusculas()
  
print(hablar('Este es un mensaje de Victor', 0.6))

# Otro ejemplo de closure
# Podemos preconfigurar una función

def mostrar(titulo):
  # Definimos la función anidada
  def saludar(mensaje):
    return titulo + '. ' + mensaje
  
  return saludar

mostrar_ing = mostrar('Ingeniero:')
mostrar_lic = mostrar('Licenciado:')

# Podemos seguir usando el estado de la función previamente configurada
# aunque el valor de titulo ya está fuera del alcance (scope)
print(mostrar_ing('Hola, soy Alvaro Ruíz'))
print(mostrar_lic('Hola, soy Ricardo'))

#######################################################################
# La función callable nos permite saber si un objeto se puede llamar o no
# todas las funciones en python son objetos
# Pero no todos los objetos en python son funciones

print(f'Se puede llamar el objeto mostrar como función?: {callable(mostrar)}')
print(f'Se puede llamar el objeto hablar como funciión?:{callable(hablar)}')
print(f'Se puede llamar el objeto mostrar_ing como funciión?:{callable(mostrar_ing)}')
print(f'Se puede llamar el objeto str como funciión?:{callable(str)}')

# Si queremos que una clase defina objetos que se puedan llamar como funciones
# tenemos que sobreescribir el método __call__
class Mostrar:
  def __init__(self, titulo):
    self.titulo = titulo
    
  def __call__(self, mensaje):
    return self.titulo + '. ' + mensaje
  
mostrar_doctor = Mostrar('doctor')

print(mostrar_doctor('Carlos Ugalde'))

