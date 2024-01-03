# Con doble guion bajo, no solo es una convención
# sino que afecta la forma en que se acceden los atributos o métodos

class Padre:
  def __init__(self):
    self.variable_publica = 1
    self._variable_protegida = 2
    self.__variable_privada = 3
    
  def get_variable_privada(self):
    return self.__variable_privada
  
  def __metodo_privado(self):
    print('Accediendo método privado padre...')
  
class Hijo(Padre):
  def __init__(self):
    super().__init__()
    self.variable_publica = 'sobreescrita 1'
    self._variable_protegida = 'sobreescrita 2'
    self.__variable_privada = 'sobrescrita 3'
    
  def __metodo_privado(self):
    print('Accediendo método privado hijo...')
    
# Prueba usando una variable global
_Prueba__variable_global = 10

#class Prueba:
#  def prueba(self):
#    return __variable_global
  
if __name__ == '__main__':
  # Imprimir todos los atributos de la clase
  padre = Padre()
  print(dir(padre))
  #print(f'Variable privada: {padre.__variable_privada}')
  print(f'Variable privada usando name mangling: {padre._Padre__variable_privada}')
  
  # Name mangling es transparente para el programador
  print(f'Acceso por medio del metodo get: {padre.get_variable_privada()}')
  
  # Prueba calse HIjo
  hijo = Hijo()
  print(f'Acceso público desde hijo: {hijo.variable_publica}')
  print(f'Acceso protegido desde hijo: {hijo._variable_protegida}')
  #print(f'Acceso privado desde hijo: {hijo.__variable_privada}')
  print(f'Acceso privado desde hijo: {hijo.get_variable_privada()}')
  
  # Prueba métodos con doble guion bajo
  # Padre.__metodo_privado necesita Name mangling
  padre._Padre__metodo_privado()
  # Hijo.__metodo_privado necesita Name mangling
  hijo._Hijo__metodo_privado()
  hijo._Padre__metodo_privado()
  
  # Accediendo a la variable global
  print(f'Accediendo variable global: {_Prueba__variable_global}')
  
  # Usando name mangling y la clase para acceder a la variable global
  #prueba = Prueba()
  #print(f'Accediendo variable global desde una clase: {prueba.prueba()}')