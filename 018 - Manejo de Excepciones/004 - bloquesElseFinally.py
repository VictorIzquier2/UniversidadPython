# Procesamiento de excepciones

resultado = None
try:
  a = int(input('Primer número: '))
  b = int(input('Segundo número: '))  
  resultado = a / b
except ZeroDivisionError as zde:
  print(f'Ocurrió un error: {zde}, {type(zde)}')
except TypeError as te:
  print(f'Ocurrió un error: {te}, {type(te)}')
except Exception as e:
  print(f'Ocurrió un error: {e}', {type(e)})
else:
  print(f'No se arrojó ninguna excepción.')
finally:
  print(f'Ejecución de bloque finally.')
  
print(f'Resultado: {resultado}')
print('continuamos...')