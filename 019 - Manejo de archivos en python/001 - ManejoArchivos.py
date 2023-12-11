# Escribir en archivos

try:
  archivo = open('prueba.txt', 'w')
  archivo.write('Agregamos información al archivo')
  archivo.write('Adios')
except Exception as e:
  print(f'Hubo un error: {e}, {type(e)}')
finally:
  archivo.close()

