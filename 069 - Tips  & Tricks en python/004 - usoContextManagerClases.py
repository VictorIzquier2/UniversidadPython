
# Manejo de Context Manager en Clases
# 1. Implementando el protocolo con las funciones(__enter__) y (__exit__)
# 2. Utilizando la librería de contextlib

# Opción 1
class ManejoArchivos:
  def __init__(self, nombre):
    self.nombre = nombre
    
  def __enter__(self):
    self.archivo = open(self.nombre, 'w', encoding='utf-8')
    return self.archivo
  
  def __exit__(self, exc_type, exc_val, exc_tb):
    try:
      self.archivo.close()
    except Exception as E:
      print(f'{E}. {exc_type} - {exc_val}: {exc_tb}')
      
if __name__ == '__main__':
  # Prueba implementando el protocolo de Context Manager
  with ManejoArchivos('prueba.txt') as archivo:
    archivo.write('prueba desde ManejoArchivo')