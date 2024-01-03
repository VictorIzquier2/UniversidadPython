from mi_modulo import funcion_publica, _funcion_protegida

class MiClase:
  def __init__(self):
    self.mi_variable_publica = 10
    self._mi_variable_protegida = 11
    
# Creamos la prueba de la clase
if __name__ == '__main__':
  objeto = MiClase()
  print(objeto.mi_variable_publica)
  # No deberíamos acceder a atributos o métodos con un guion bajo al inicio
  print(objeto._mi_variable_protegida)
  
  # Accedemos a las funciones del modulo importado
  funcion_publica()
  _funcion_protegida()