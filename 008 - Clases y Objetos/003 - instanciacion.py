# instanciación en Python

class Persona:
  # Atributos de clase
  def __init__(self, nombre, apellido, edad):
    # Atributos de Instancia
    self.nombre: str = nombre
    self.apellido: str = apellido
    self.edad: int = edad
    pass 


persona1 = Persona('Víctor', 'Izquierdo', 38)
persona2 = Persona('Karla', 'Gomez', 29)

print(persona1.nombre + " " + persona1.apellido + " " + str(persona1.edad))
print(persona2.nombre + " " + persona2.apellido + " " + str(persona2.edad))
