# Generadores
# Es una función especial en python
# Regresan una secuencia de valores a través de un método de produccion
# Suspende la ejecución de la función por medio de la palabra reservada yield
# Sutituye a return

def generador():
  yield 1
  print('Se reanuda la ejecución')
  yield 2
  print('Se reanuda la ejecución')
  yield 3
  
# Consumimos el generador a demanda
gen = generador()

# Con cada llamada consumimos un valor
print(next(gen))
print(next(gen))
print(next(gen))
# Si tratamos de consumir más valores de los que produce el generador
# lanza un error de StopIteration
# print(next(gen)) Error Stop Iteration

# Consumiendo los valores del generador con un ciclo for
for valor in generador():
  print(f'Número generado: {valor}')