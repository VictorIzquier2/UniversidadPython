# Escribir en archivos

try:
  archivo = open('prueba.txt', 'w', encoding='UTF8')
  archivo.write('Agregamos información al archivo\n')
  archivo.write('Adios')
except Exception as e:
  print(f'Hubo un error: {e}, {type(e)}')
finally:
  archivo.close()
