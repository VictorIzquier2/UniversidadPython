# Clases en Python

class Persona:
  # Atributos de clase
  def __init__(self):
    # Atributos de Instancia
    self.nombre: str = 'Juan'
    self.apellido: str = 'Perez'
    self.edad: int = 28
    pass 


persona1 = Persona()

print(persona1.nombre + " " + persona1.apellido)