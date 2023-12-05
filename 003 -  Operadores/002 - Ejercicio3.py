"""
Instrucciones:

Calcular el área y el perímetro de un rectángulo con las variables alto (int) y ancho (int)

"""

def rectangulo():
  alto: int = int(input("Introduce el alto del rectángulo: "))
  ancho: int = int(input("Introduce el ancho del rectángulo: "))
  perimetro: int = 2 * (alto + ancho)
  area: int = alto * ancho
  print(f"Area: {area}\nPerímetro: {perimetro}\n")
  
rectangulo()