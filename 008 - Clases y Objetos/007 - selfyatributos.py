# Self en Python es como this en Java
# NO tiene porqué llamarse self

class Persona:
  # Atributos de clase
  def __init__(this, nombre, apellido, edad):
    # Atributos de Instancia
    this.nombre: str = nombre
    this.apellido: str = apellido
    this.edad: int = edad
    pass
  
  def mostrar_detalle(this):
    print(f"Persona: {this.nombre} {this.apellido} {this.edad}")
    pass


persona1 = Persona('Víctor', 'Izquierdo', 38)
persona2 = Persona('Karla', 'Gomez', 29)

Persona.mostrar_detalle(persona1)

# Añadir nuevos atributos (al vuelo)
persona1.telefono = '662 086 316'
print(persona1.telefono)