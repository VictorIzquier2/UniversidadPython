class Persona:
  contador_personas = 0
  
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido
    
#Mostrar los atributos de un objeto
persona1 = Persona('Juan', 'Perez')
print(persona1.__dict__)

# Crear un atributo al vuelo
print(persona1.contador_personas)
# persona1.