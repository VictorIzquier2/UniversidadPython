# Clase Cubo con método Volumen

class Cubo():
  """ 
  Clase Cubo que delimita una figura geométrica por su base, altura y ancho. Permite calcular el volumen del mismo
  """
  
  def __init__(self, base, altura, ancho):
    self.base = base
    self.altura = altura
    self.ancho = ancho
  
  def volumenCubo(self):
    resultado = self.base * self.altura * self.ancho
    return resultado
  
base = int(input("Introduce la base del cubo: "))
altura= int(input("Introduce la altura del cubo: "))
ancho = int(input("Introduce el ancho del cubo: "))
  
cubo1 = Cubo(base, altura, ancho)
print(f"El volumen del cubo es: {cubo1.volumenCubo()}")