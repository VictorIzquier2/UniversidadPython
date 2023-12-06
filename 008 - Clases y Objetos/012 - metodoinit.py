# Haciendo más robusto el método init de la clase Persona

class Persona:
  
  def __init__(self, nombre, apellido, edad, *valores, **terminos):
  
    self.nombre: str = nombre
    self.apellido: str = apellido
    self.edad: int = edad
    self.valores = valores
    self.terminos = terminos
    
  
  def mostrar_detalle(self):
    print(f"Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}")
    


persona1 = Persona('Víctor', 'Izquierdo', 38, '662 086 316', 2, 3, 5, m='manzana', p='platano', a='aguacate')
persona2 = Persona('Karla', 'Gomez', 29)

Persona.mostrar_detalle(persona1)