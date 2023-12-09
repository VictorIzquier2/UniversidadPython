class Monitor:
  contador_monitores = 0
  def __init__(self, marca, tamaño):
    Monitor.contador_monitores += 1
    self._id_monitor = Monitor.contador_monitores
    self._marca = marca
    self._tamaño = tamaño
    
  @property
  def id_monitor(self):
    return self._id_monitor
  
  @id_monitor.setter
  def id_monitor(self, id_monitor):
    self._id_monitor = id_monitor
  
  @property
  def marca(self):
    return self._marca
  
  @marca.setter
  def marca(self, marca):
    self._marca = marca
    
  @property
  def tamaño(self):
    return self._tamaño
  
  @tamaño.setter
  def tamaño(self, tamaño):
    self._tamaño = tamaño
    
  def __str__(self) -> str:
    return f'Id: {self.id_monitor}, Marca: {self.marca}, Tamaño: {self.tamaño}'
    
if __name__ == '__main__':
  monitor1 = Monitor('HP', 15)
  print(monitor1)
  monitor2 = Monitor('Acer', 27)
  print(monitor2)