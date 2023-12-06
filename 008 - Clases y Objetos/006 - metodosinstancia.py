# instanciación en Python

class Persona:
  # Atributos de clase
  def __init__(self, nombre, apellido, edad):
    # Atributos de Instancia
    self.nombre: str = nombre
    self.apellido: str = apellido
    self.edad: int = edad
    pass
  
  def mostrar_detalle(self):
    print(f"Persona: {self.nombre} {self.apellido} {self.edad}")
    pass


persona1 = Persona('Víctor', 'Izquierdo', 38)
persona2 = Persona('Karla', 'Gomez', 29)

persona1.mostrar_detalle()
persona2.mostrar_detalle()

persona1.nombre = 'Victor Jesús'
persona1.mostrar_detalle()