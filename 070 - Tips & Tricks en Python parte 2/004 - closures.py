#################################################################
# Closures
# Las funciones internas pueden capturar y guardar el estado de la función externa

def hablar(texto, volumen):
  # La función interna ya no recibe parámetros
  # Utiliza el estado de la función padre (externa)
  def minusculas():
    return texto.lower()
  
  def mayusculas():
    return texto.upper()
  
  if volumen > 0.5:
    return mayusculas()
  else:
    return minusculas()
  
print(hablar('Este es un mensaje de Victor', 0.6))

# Otro ejemplo de closure
# Podemos preconfigurar una función

def mostrar(titulo):
  # Definimos la función anidada
  def saludar(mensaje):
    return titulo + '. ' + mensaje
  
  return saludar

mostrar_ing = mostrar('Ingeniero:')
mostrar_lic = mostrar('Licenciado:')

# Podemos seguir usando el estado de la función previamente configurada
# aunque el valor de titulo ya está fuera del alcance (scope)
print(mostrar_ing('Hola, soy Alvaro Ruíz'))
print(mostrar_lic('Hola, soy Ricardo'))


    
