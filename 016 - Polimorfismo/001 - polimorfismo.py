# Polimorfismo

from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
  print(objeto)
  print(type(objeto))
  print(objeto.mostrar_detalles())
  
empleado1 = Empleado('Juan', 5000)
imprimir_detalles(empleado1)
gerente1 = Gerente('Carlos', 7500, 'Congelados')
imprimir_detalles(gerente1)

  