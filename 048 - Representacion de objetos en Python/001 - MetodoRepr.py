# Representación de objetivos (str, repr, format)

# print(dir(object))

class Persona:
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido
    
  # repr, más enfocado a los programadores
  def __repr__(self):
    return f'Persona(nombre:{self.nombre}, apellido:{self.apellido})'
  
persona1 = Persona('Juan', 'Pérez')
print(f'{persona1!r}')
  