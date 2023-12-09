# Métodos estáticos

class MiClase:
  variable_clase = 'Valor variable clase'
  
  def __init__(self, variable_instancia):
    self.variable_instancia = variable_instancia
    
  @staticmethod
  def metodo_estatico():
    MiClase.variable_clase = 'Valor variable clase modificado'
    
  @classmethod
  def metodo_clase(cls):
    print(cls.variable_clase)
    
MiClase.metodo_clase()