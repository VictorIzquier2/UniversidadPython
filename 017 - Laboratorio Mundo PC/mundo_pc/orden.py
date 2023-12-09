class Orden():
  contador_ordenes = 0
  
  def __init__(self, computadoras):
    Orden.contador_ordenes += 1
    self._id_orden = Orden.contador_ordenes
    self._computadoras = list(computadoras)
    
  @property
  def id_orden(self):
    return self._id_orden
  
  @id_orden.setter
  def id_orden(self, id_orden):
    self._id_orden = id_orden
    
  @property
  def computadoras(self):
    return self._computadoras
  
  @computadoras.setter
  def computadoras(self, computadoras):
    self._computadoras = computadoras
    
  def agregar_computadora(self, computadora):
    self._computadoras.append(computadora)
  
  def __str__(self):
    computadoras_str = ''
    for computadora in self.computadoras:
      computadoras_str += computadora.__str__()
    return f'''
    Orden: {self.id_orden}
    Computadoras: {computadoras_str}
    '''