# Operadores lógicos

a: bool = False
b: bool = False
c: bool = True
d: bool = True

def a_and_b(a, b):
  resultado = a and b
  print(f"Resultado a and b: {resultado}")
  
def a_or_b(a, b):
  resultado = a or b
  print(f"Resultado a or b: {resultado}")

a_and_b(a,b)
a_or_b(a,b)
a_and_b(c,d)
a_or_b(b,c)


