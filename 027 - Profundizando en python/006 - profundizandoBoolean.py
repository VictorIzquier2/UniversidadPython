# Profundizando en Boolean (True o False)

# Tipos numéricos, False para 0, True para los demás valores
valor = 0
print(f'Valor: {bool(valor)}')
valor = 1
print(f'Valor: {bool(valor)}')

# Tipo str, False para '', True para todos los demás valores
valor = ''
print(f'Valor: {bool(valor)}')
valor = 'Hola'
print(f'Valor: {bool(valor)}')

# Tipo colecciones, False para vacías, True para todos los demás
# Lista
valor = []
print(f'Valor: {bool(valor)}')
valor =['Karen']
print(f'Valor: {bool(valor)}')

# Tupla:
valor = ()
print(f'Valor: {bool(valor)}')
valor = (5)
print(f'Valor: {bool(valor)}')

# Diccionario:
valor = {}
print(f'Valor: {bool(valor)}')
valor = {'username': 'usuario'}
print(f'Valor: {bool(valor)}')


