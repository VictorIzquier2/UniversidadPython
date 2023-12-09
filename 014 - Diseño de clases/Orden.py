from Producto import Producto

class Orden:
  contador_ordenes = 0
  
  def __init__(self, productos):
    Orden.contador_ordenes += 1
    self._id_orden = Orden.contador_ordenes
    self._productos = list(productos)
    
  @property
  def id_orden(self):
    return self._id_orden
  
  @id_orden.setter
  def id_orden(self, id_orden):
    self._id_orden = id_orden
    
  @property
  def productos(self):
    return self._productos
  
  @productos.setter
  def productos(self, productos):
    self._productos = productos
    
  def agregar_producto(self, producto):
    self.productos.append(producto)
  
  def calcular_total(self):
    total = 0
    for producto in self.productos:
      total += producto.precio
    return total
  
  def __str__(self):
    productos_str = ''
    for producto in self.productos:
      productos_str += producto.__str__() + ' | '
    return f'orden: {self.id_orden}, Productos: {productos_str}'
  
if __name__ == '__main__':
  producto1 = Producto('Camisa', 100.00)
  producto2 = Producto('Pantalón', 150.00)
  producto3 = Producto('Calcetines', 50.00)
  productos = [producto1, producto2]
  orden1 = Orden(productos)
  orden1.agregar_producto(producto3)
  print(orden1)
  print(f'Total orden1: {orden1.calcular_total()}')
  
      