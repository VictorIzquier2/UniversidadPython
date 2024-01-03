# Aserciones
# Tip. Las aserciones nos pueden ayudar a depurar nuestros programas de errores que no nos podemos recuperar

# Ejemplo 1. Revisamos si la división es entre 0

def dividir(a, b):
  # Nos aseguramos que el valor de b no es 0 para poder continuar con nuestro programa
  try:
    assert b != 0, 'División entre cero'
  except AssertionError as AE:
    print(f'Error de aserción: {AE}')
  else:
    print(f'Resultado: {a} / {b} = {a/b}')  
  
# Ejemplo 2. Realizamos el cálculo del promedio de una lista de calificaciones
def obtener_promedio(calificaciones):
  # Si la lista de calificaciones está vacía no debería continuar el programa
  try:
    assert len(calificaciones) != 0, 'La lista de calificaciones está vacía'
  except AssertionError as AE:
    print(f'Error de aserción: {AE}')
  else:
    print(f'El promedio de calificaciones es: {sum(calificaciones)/len(calificaciones)}')
  
# Ejemplo 3. Realizamos un descuento al producto proporcionado
def aplicar_descuento(productos, descuento):
  precio_con_descuento = int(productos['precio'] * (1.0 - descuento))
  try:
    assert 0 <= precio_con_descuento <= productos['precio'], f'Descuento Inválido: {precio_con_descuento}'
  except AssertionError as AE:
    print(f'Error de aserción: {AE}')
  else:
    print(f'Nuevo precio del producto: {precio_con_descuento}')
if __name__ == '__main__':
  # Prueba ejemplo 1. División entre cero
  dividir(10,2)
  dividir(10,0)
  
  # Prueba ejemplo 2. Cálculo promedio de calificaciones
  calificaciones = [10, 8, 7, 9]
  obtener_promedio(calificaciones)
  obtener_promedio([])
  
  # Prueba ejemplo 3. Aplicar descuento
  productos = {'nombre': 'Camisa', 'precio':1500}
  aplicar_descuento(productos, 0.10)
  aplicar_descuento(productos, 1.2)
  
  