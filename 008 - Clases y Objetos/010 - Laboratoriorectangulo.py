# Clase Rectangulo con método Area

class Rectangulo():
  """ 
  Clase Rectángulo que delimita una figura geométrica por su base, altura y permite calcular el área
  """
  
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura
  
  def areaRectangulo(self):
    resultado = self.base * self.altura
    return resultado
  
base = int(input("Introduce la base del rectángulo: "))
altura= int(input("Introduce la altura del rectángulo: "))
  
rectangulo1 = Rectangulo(base, altura)
print(f"El área del rectángulo es: {rectangulo1.areaRectangulo()}")