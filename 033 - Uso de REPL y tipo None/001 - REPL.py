class Persona:
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido
    
  def __str__(self):
    return f'Persona: [Nombre: {self.nombre}, Apellido: {self.apellido}, id: {hex(id(self)).upper()}]'

def mostrar_mensaje(mensaje):
  print(mensaje)

if __name__ == '__main__':  
  persona1 = Persona('Juan', 'Pérez')
  mostrar_mensaje(persona1)
