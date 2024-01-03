from contextlib import contextmanager


# Manejo de Context Manager en Clases
# 1. Implementando el protocolo con las funciones(__enter__) y (__exit__)
# 2. Utilizando la librería de contextlib

# Opción 2

# Este metodo es un generador, en primer lugar adquiere el recurso
# Luego suspende temporalmente la ejecución al utilizar yield
# Cuando termina de ser utilizado este método, regresa a la ejecución y cierra el recurso que se ha utilizado
@contextmanager
def manejador_archivos(nombre):
  try:
    archivo = open(nombre, 'w', encoding='utf-8')
    yield archivo
  finally:
    archivo.close()
    
# Ejercicio de Identador
class Indentador():
  def __init__(self):
    self.nivel = 0
  
  def __enter__(self):
    self.nivel += 1
    return self
  
  def __exit__(self, exc_type, exc_val, exc_tb):
    self.nivel -= 1
  
  def imprimir(self, texto):
    print('   '*self.nivel + texto)
    
if __name__ == '__main__':
  # Prueba con la librería contextlib
  with manejador_archivos('prueba.txt') as archivo:
    archivo.write('prueba desde decorador')
    archivo.write('\nadios')
    
    # Prueba de Identador
    with Indentador() as indentador:
      indentador.imprimir('primer nivel')
      with indentador:
        indentador.imprimir('segundo nivel')
        indentador.imprimir('continúa el segundo nivel...')
        with indentador:
          indentador.imprimir('tercer nivel')
          indentador.imprimir('continúa el tercer nivel...')
      indentador.imprimir('fin primer nivel')