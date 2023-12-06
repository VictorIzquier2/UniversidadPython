# Definir una clase padre Vehiculo y dos clases hijas: coche y bicicleta


class Vehiculo():
  def __init__(self, color, ruedas):
    self._color: str = color
    self._ruedas: int = ruedas
    
  @property
  def color(self):
    return self._color
  
  @color.setter
  def color(self, color):
    if not isinstance(color, str):
      raise ValueError("El color debe ser una cadena de caracteres.")
    self._color = color
    
  @property
  def ruedas(self):
    return self._ruedas
    
  @ruedas.setter
  def ruedas(self, ruedas):
    if ruedas < 1:
      raise ValueError("Las ruedas no pueden ser menores que cero")
    self._ruedas = ruedas
      
    
  def __str__(self):
    return f"Color: {self.color}. Ruedas:{self.ruedas}"
  
class Coche(Vehiculo):
  def __init__(self, color, ruedas, velocidad):
    super().__init__(color, ruedas)
    self._velocidad: int = velocidad
    
  @property
  def velocidad(self):
    return self._velocidad
  
  @velocidad.setter
  def velocidad(self, velocidad):
    if velocidad < 0:
      raise ValueError("La velocidad no puede ser un valor negativo.")
    self._velocidad = velocidad
    
  def __str__(self):
    return f'{super().__str__()} Velocidad: {self.velocidad}'
  
class Bicicleta(Vehiculo):
  def __init__(self, color, ruedas, tipo):
    super().__init__(color, ruedas)
    self._tipo: str = tipo
    
  @property
  def tipo(self):
    return self._tipo
  
  @tipo.setter
  def tipo(self, tipo):
    if not isinstance(tipo, str):
      raise ValueError("El tipo de bicicleta debe ser una cadena de caracteres.")
    self._tipo = tipo
    
  def __str__(self):
    return f'{super().__str__()}. Tipo: {self.tipo}'

if __name__ == '__main__':
  coche1 = Coche('Rojo', 4, 50)
  bicicleta1 = Bicicleta('Verde', 2, 'Paseo')
  print(coche1)
  print(bicicleta1)

  