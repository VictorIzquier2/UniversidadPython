# Operador +

a = 2
b = 3
print(a + b)

a = 'Hola '
b = 'mundo'
print(a + b)

a = [1,2,3]
b = [4,5,6]
print(a + b)

class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
    
  def __add__(self, other):
    return f'{self.nombre} y {other.nombre}'
  
  def __sub__(self, other):
    return self.edad - other.edad
  
persona1 = Persona('Juan', 28)
persona2 = Persona('Carlos', 50)
print(persona1 + persona2)
print(persona1 - persona2)