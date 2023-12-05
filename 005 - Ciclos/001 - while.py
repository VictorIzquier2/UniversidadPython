condicion = True
contador = 0

while condicion:
  print('Ejecutando ciclo while')
  contador += 1
  
  if contador >= 5:
    condicion = False
else:
  print('Fin del ciclo while')