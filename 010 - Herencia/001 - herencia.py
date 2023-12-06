from Persona import Persona

class Empleado(Persona):
  def __init__(self, nombre, apellido, edad, sueldo):
    super().__init__(nombre, apellido, edad)
    self.sueldo = sueldo
    
empleado1 = Empleado('Juan', 'Tanamera', 50, 5000)
print(empleado1)
print(empleado1.sueldo)