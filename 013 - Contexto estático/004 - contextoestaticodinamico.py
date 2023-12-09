# Contextos estático y dinámico

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
    
  def metodo_instancia(self):
    self.metodo_clase()
    self.metodo_estatico()
    print(self.variable_clase)
    print(self.variable_instancia)
    
miObjeto1 = MiClase('variable_instancia')
miObjeto1.metodo_instancia()