# Excepciones

"""
BaseException
      Exception
            ArithmeticError
                  ZeroDivisionError
                  
            OSError
                  FileNotFoundError
                  PermissionError
                  
            RuntimeError
            
            TypeError
            
            LookupError
                  IndexError
                  KeyError
                  
            SytaxError
                  IndentationError   
"""

resultado = None
a = '10'
b = 0  
try:
  resultado = a / b
except ZeroDivisionError as zde:
  print(f'Ocurrió un error: {zde}, {type(zde)}')
except TypeError as te:
  print(f'Ocurrió un error: {te}, {type(te)}')
except Exception as e:
  print(f'Ocurrió un error: {e}', {type(e)})
  
print(f'Resultado: {resultado}')
print('continuamos...')