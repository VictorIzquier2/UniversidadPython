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
    
if __name__ == '__main__':
  # Prueba con la librería contextlib
  with manejador_archivos('prueba.txt') as archivo:
    archivo.write('prueba desde decorador')
    archivo.write('\nadios')