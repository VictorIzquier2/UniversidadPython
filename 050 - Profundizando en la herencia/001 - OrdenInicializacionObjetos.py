# Orden de inicialización de objetos
class Padre:
  def __init__(self):
    print('Inicializador Padre')
    
  def metodo(self):
    print('Metodo padre')
    
class Hijo(Padre):
  # Se manda a llamar el método __ini__ de la clase padre
  # siempre y cuando la clase hija no defina su propio método init
  
  # Definimos el método init
  def __init__(self):
    print('Inicializador Hijo')
    super().__init__()
    
  # Sobreescribimos el método heredado de la clase padre
  def metodo(self):
    print('Metodo sobreescrito hijo')
    super().metodo()
    
#padre1 = Padre()
#padre1.metodo()
hijo1 = Hijo()
hijo1.metodo()

