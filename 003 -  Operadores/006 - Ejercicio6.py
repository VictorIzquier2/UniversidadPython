# Dentro de rango

def rango(valorMin, valorMax):
  valor = int(input("Escribe un valor de rango: "))
  dentroRango: bool = (valor >= valorMin) and (valor <= valorMax)
  if (dentroRango):
    print(f"El valor {valor} está dentro del rango de {valorMin} a {valorMax}.")
  else:
    print(f"El valor {valor} está fuera de rango.") 
    
rango(0,5)