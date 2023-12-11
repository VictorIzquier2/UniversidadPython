# Copiar archivos

try:
  archivo2 = open('copia.txt', 'a', encoding='utf8')
  archivo = open('prueba.txt', 'r', encoding='utf8')
  archivo2.write(archivo.read())
  #for linea in archivo:
    #print(linea)
  #print(archivo.readlines())
except Exception as e:
  print(f'Hubo un error: {e}, {type(e)}')
finally:
  archivo.close()
