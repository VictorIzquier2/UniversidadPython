from Persona import Persona

class Empleado(Persona):
  def __init__(self, nombre, apellido, edad, sueldo):
    super().__init__(nombre, apellido, edad)
    self._sueldo = sueldo
    
  @property
  def sueldo(self):
    return self._sueldo
  
  @sueldo.setter
  def sueldo(self, sueldo):
    if sueldo < 0:
      raise ValueError("El sueldo no puede ser un valor negativo.")
    self._sueldo = sueldo
    
  def __str__(self):
    return f'{super().__str__()} {self.sueldo}'
    
empleado1 = Empleado('Juan', 'Tanamera', 50, 5000)
print(empleado1)