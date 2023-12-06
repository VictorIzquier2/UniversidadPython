# Aritmetica

class Aritmetica:
  """
  Clase Aritmetica para realizar las operaciones de sumar, restar, multiplicar y dividir con un número indeterminado de operandos.
  """
  
  def __init__(self, *operandos):
    self.operandos = operandos
    
  def sumar(self):
    return sum(self.operandos)
  
  def restar(self):
    resultado = self.operandos[0]
    for operando in self.operandos[1:]:
      resultado-= operando
    return resultado

  def multiplicar(self):
    resultado = 1
    for operando in self.operandos:
      resultado *= operando
    return resultado
  
  def dividir(self):
    try:
      resultado = self.operandos[0]
      for operando in self.operandos[1:]:
        resultado /= operando
      return resultado
    except ZeroDivisionError:
      return "Error: División por cero"


operacion1 = Aritmetica(12,4,3)
print(operacion1.sumar())
print(operacion1.restar())
print(operacion1.multiplicar())
print(operacion1.dividir())
      
    
    
  

