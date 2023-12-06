# Encapsulamiento en Python

class Persona:
  
  def __init__(self, nombre, apellido, edad):
  
    self._nombre: str = nombre
    self.apellido: str = apellido
    self.edad: int = edad
    
  
  def mostrar_detalle(self):
    print(f"Persona: {self._nombre} {self.apellido} {self.edad}")
    


persona1 = Persona('Víctor', 'Izquierdo', 38)
persona1._nombre = 'Víctor Jesús' # No se debería de poder acceder directamente a un atributo de esta manera. Necesitamos encapsular el código
Persona.mostrar_detalle(persona1)