# Get y Set para encapsular una clase

class Persona:
  
  def __init__(self, nombre, apellido, edad):
  
    self._nombre: str = nombre
    self._apellido: str = apellido
    self._edad: int = edad
  
  # Para acceder al atributo _nombre necesitamos un decorador
  @property
  def nombre(self):
    return self._nombre
  
  @nombre.setter
  def nombre(self, nombre):
    # validación nombre sea una cadena de caracteres
    if not isinstance(nombre, str):
      raise ValueError("El nombre debe ser una cadena de caracteres")
    self._nombre = nombre
    
  def __str__(self):
    return f"Persona: {self.nombre} {self._apellido} {self._edad}"
    


persona1 = Persona('Víctor', 'Izquierdo', 38)
persona1.nombre ='Víctor Jesús'
print(persona1.nombre)