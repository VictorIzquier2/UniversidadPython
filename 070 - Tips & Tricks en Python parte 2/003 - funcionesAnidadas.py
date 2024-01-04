# como almacenar una función en una estructura de datos (list)
def mayusculas(texto):
  return texto.upper()

variable_funcion = mayusculas

lista_funciones = [mayusculas, variable_funcion, str.upper]
print(lista_funciones)

for function in lista_funciones:
  print(function, function('Saludos desde la función'))
  
# 0 podemos acceder directamente a la función que deseemos
print(lista_funciones[1]('Saludos desde variables_funcion'))


# Podemos pasar funciones a otras funciones
# Este tipo de funciones se conocen como higher-order functions

def saludar(argumento_funcion):
  # Usamos la función que recibimos como argumento y devolvemos la referencia
  referencia_funcion_retornada = argumento_funcion('Hola, Saludos desde mi función')
  print(referencia_funcion_retornada)
  
# Llamamos la función saludar, pasamos la referencia de una función como argumento
saludar(mayusculas)

# Podemos pasar una nueva implementación de la función que pasamos como argumentos
def minusculas(texto):
  return texto.lower()

saludar(minusculas)

# El clásico ejemplo de higher-order functions es la función map
# Esta función toma una función como referencia, y un iterable, llama a la función
# en cada elemento del iterable proporcionado

print(list(map(mayusculas, ['texto1', 'texto2', 'texto3'])))
print(list(map(minusculas, ['Texto1', 'Texto2', 'Texto3'])))


################################################################
# Funciones anidadas

def mostrar(texto):
  # Definición de la función interna o anidada
  def convertir_minusculas(cadena):
    return cadena.lower()
  
  # Una vez definida la función interna, la mandamos llamar
  return convertir_minusculas(texto)
  
# Cada vez que se llama la función mostrar
# se crea la función interna convertir_minusculas
print(mostrar('Desde Función Anidada...'))

# No podemos utilizar la función interna desde fuera de la función externa
#print(mostrar.convertir_minusculas('Texto1'))

# Retornar la función anidada
# Observar que en ningún momento se llama la función anidada desde la función
def hablar(volumen):
  
  def minusculas(texto):
    return texto.lower()
  
  def mayusculas(texto):
    return texto.upper()
  
  if volumen > 0.5:
    return mayusculas
  else:
    return minusculas
  
# Utilizamos la función anidada
print(hablar(0.6)('hablo fuerte...'))
print(hablar(0.2)('hablo silencioso'))

variable_minusculas = hablar(0.4)
print(variable_minusculas('hablo Suave Nuevamente'))
  
  
