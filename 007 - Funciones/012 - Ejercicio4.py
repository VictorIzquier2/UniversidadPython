# Calculadora de impuestos

def calculadoraImpuestos():
  cantidad = float(input("Introduzca la cantidad a pagar: "))
  porcentaje = float(input("Introduzca el porcentaje de impuestos: "))
  impuesto: float = (cantidad / 100) * porcentaje
  total: float = cantidad + impuesto
  print(f"Pago con impuestos: {total}")
  
  
calculadoraImpuestos()