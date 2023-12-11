
# Leer todos los caracteres del archivo

try:
  archivo = open('prueba.txt', 'r', encoding='utf8')
  #print(archivo.read())
except Exception as e:
  print(f'Hubo un error: {e}, {type(e)}')
finally:
  archivo.close()
  
  
# Leer solo algunos caracteres
  
try:
  archivo = open('prueba.txt', 'r', encoding='utf8')
  #print(archivo.read(5)) # indicamos el número de caracteres que queremos leer
except Exception as e:
  print(f'Hubo un error: {e}, {type(e)}')
finally:
  archivo.close()
  
# Leer lineas completas

try:
  archivo = open('prueba.txt', 'r', encoding='utf8')
  #print(archivo.readline())
  #print(archivo.readline())
except Exception as e:
  print(f'Hubo un error: {e}, {type(e)}')
finally:
  archivo.close()
  
  
# Iterar cada una de las líneas

try:
  archivo = open('prueba.txt', 'r', encoding='utf8')
  #for linea in archivo:
    #print(linea)
  #print(archivo.readlines())
  print(archivo.readlines()[1])
except Exception as e:
  print(f'Hubo un error: {e}, {type(e)}')
finally:
  archivo.close()



