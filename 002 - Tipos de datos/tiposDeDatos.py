# Tipos de datos en Python

""" Numérico 
      Integer
      Numero complejo
      Float
    
    Diccionario
  
    Booleano
  
    Set
  
    De tipo secuencia
      Cadenas de texto
      Listas
      Tuplas
"""

def imprimirTipo(x):
  print(f"Variable: {x}\nTipo de variable: {type(x)}\n")

x: int = 10
y: str = "Hola Mundo"
z: bool = True
f: float = 10.5
  
imprimirTipo(x)
imprimirTipo(y)
imprimirTipo(z)
imprimirTipo(f)
