
with open('prueba.txt', 'w', encoding='utf-8') as archivo:
  archivo.write('Hola desde Python')
  
# Esto es equivalente a:
archivo = open('prueba.txt', 'w', encoding='utf-8')
try:
  archivo.write('Hola desde Pyhton')
finally:
  archivo.close()

# Esto NO es equivalente
archivo = open('prueba.txt', 'w', encoding='utf-8')
archivo.write('Hola sin with')
# Esto no asegura el cierre de recursos en caso de error
archivo.close()

  