# Procesamiento de excepciones

resultado = None
try:
  a = int(input('Primer número: '))
  b = int(input('Segundo número: '))  
  resultado = a / b
except Exception as e:
  print(f'Ocurrió un error: {e}', {type(e)})
  
print(f'Resultado: {resultado}')
print('continuamos...')