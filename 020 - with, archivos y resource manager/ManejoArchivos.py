class ManejoArchivos(object):
  def __init__(self, nombre):
    self._nombre = nombre
    
  @property
  def nombre(self):
    return self._nombre
  
  @nombre.setter
  def nombre(self, nombre):
    self._nombre = nombre
    
  def __enter__(self):
    print('Obtenemos el recurso'.center(50,'-'))
    self.nombre = open(self.nombre, 'r', encoding='utf8')
    return self.nombre
  
  def __exit__(self, tipo_excepcion, valor_excepcion, texto_error):
    print('Cerramos el recurso'.center(50,'-'))
    try:
      if self.nombre:
        self.nombre.close()
    except Exception as e:
      print(f'{tipo_excepcion}. {valor_excepcion}\n\t{texto_error}')
    else:
      print("Archivo cerrado correctamente")
    