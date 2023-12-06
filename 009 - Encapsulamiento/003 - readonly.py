# Read-only

class Persona:
  
  def __init__(self, nombre, apellido, edad):
  
    self._nombre: str = nombre
    self._apellido: str = apellido
    self._edad: int = edad
  
  @property
  def nombre(self):
    return self._nombre
  
  # Si no añadimos un setter el atributo queda como read-only
    
  def __str__(self):
    return f"Persona: {self.nombre} {self._apellido} {self._edad}"
    


persona1 = Persona('Víctor', 'Izquierdo', 38)
persona1.nombre ='Víctor Jesús'
print(persona1.nombre)