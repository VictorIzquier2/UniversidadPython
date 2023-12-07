class FiguraGeometrica():
  def __init__(self, ancho, alto):
    self._ancho = ancho
    self._alto = alto
    
  @property
  def ancho(self):
    return self._ancho
  
  @ancho.setter
  def ancho(self, ancho):
    self._ancho = ancho
    
  @property
  def alto(self):
    return self._alto
  
  @alto.setter
  def alto(self, alto):
    self._altho = alto
    
class Color():
  def __init__(self, color):
    self._color = color
    
  @property
  def color(self):
    return self._color
  
  @color.setter
  def ancho(self, color):
    self._color = color
    
class Cuadrado(FiguraGeometrica, Color):
  def __init__(self, lado, color):
    FiguraGeometrica.__init__(self, lado, lado)
    Color.__init__(self, color)
    
  def area(self):
    return self.alto * self.ancho
  
  
if __name__ == '__main__':
  cuadrado1 = Cuadrado(5, 'rojo')
  print(f"El alto del cuadrado es: {cuadrado1.alto}")
  print(f"El ancho del cuadrado es: {cuadrado1.ancho}")
  print(f"El color del cuadrado es: {cuadrado1.color}")
  print(f"El área del cuadrado es: {cuadrado1.area()}") 
  
  print(Cuadrado.mro())