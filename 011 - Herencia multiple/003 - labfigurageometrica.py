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
    
  def __str__(self) -> str:
    return f'FiguraGeometrica [Ancho: {self.ancho}, Alto: {self.alto}]'
  
class Color():
  def __init__(self, color):
    self._color = color
    
  @property
  def color(self):
    return self._color
  
  @color.setter
  def ancho(self, color):
    self._color = color
    
  def __str__(self) -> str:
    return f'Color [color: {self.color}]'
    
class Cuadrado(FiguraGeometrica, Color):
  def __init__(self, lado, color):
    FiguraGeometrica.__init__(self, lado, lado)
    Color.__init__(self, color)
    
  def area(self):
    return self.alto * self.ancho
  
  def __str__(self) -> str:
    return f'Cuadrado: {FiguraGeometrica.__str__(self)} {Color.__str__(self)}'
  
class Rectangulo(FiguraGeometrica, Color):
  def __init__(self, ancho, alto, color):
    FiguraGeometrica.__init__(self, ancho, alto)
    Color.__init__(self, color)
    
  def area(self):
    return self.ancho * self.alto
  
  def perimetro(self):
    return 2*(self.ancho + self.alto)
  
  def __str__(self) -> str:
    return f'Rectángulo: {FiguraGeometrica.__str__(self)} {Color.__str__(self)}'
  
  
if __name__ == '__main__':
  cuadrado1 = Cuadrado(5, 'rojo')
  print(f"El alto del cuadrado es: {cuadrado1.alto}")
  print(f"El ancho del cuadrado es: {cuadrado1.ancho}")
  print(f"El color del cuadrado es: {cuadrado1.color}")
  print(f"El área del cuadrado es: {cuadrado1.area()}") 
  print(cuadrado1)
  
  rectangulo1 = Rectangulo(5, 4, 'verde')
  print(f"El alto del rectángulo es: {rectangulo1.alto}")
  print(f"El ancho del rectángulo es: {rectangulo1.ancho}")
  print(f"El color del rectángulo es: {rectangulo1.color}")
  print(f"El área del rectángulo es: {rectangulo1.area()}")
  print(f"El perímetro del rectángulo es: {rectangulo1.perimetro()}")
  print(rectangulo1)