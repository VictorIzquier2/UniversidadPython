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
    
  @property
  def apellido(self):
    return self._apellido
  
  @apellido.setter
  def apellido(self, apellido):
    # Validación apellido sea una cadena de caracteres
    if not isinstance(apellido, str):
      raise ValueError("El apellido debe ser una cadena de caracteres")
    self._apellido = apellido
    
  @property
  def edad(self):
    return self._edad
  
  @edad.setter
  def edad(self, edad):
    # Validación edad no sea negativa
    if edad < 0:
      raise ValueError("La edad no puede ser negativa.")
    self._edad = edad
    
  def __str__(self):
    return f"Persona: {self.nombre} {self.apellido} {self.edad}"
  
  def __del__(self):
    print(f'Persona: {self.nombre} {self.apellido} fue destruido')
    

if __name__ == '__main__':
  persona1 = Persona('Víctor', 'Izquierdo', 38)
  persona1.nombre ='Víctor Jesús'
  print(persona1.nombre)