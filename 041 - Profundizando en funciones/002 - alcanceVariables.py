

# Scope

var_global = 'Variable global'

def imprimir():
  global var_global
  # Acceder a una variable global
  print(f'Variable global desde función: {var_global}')
  
  # Definición de variable local
  var_local = 'Variable local'
  print(f'Variable local desde función: {var_local}')
  var_global = 'Nuevo valor variable global'
  
  def funcion_anidada():
    print(f'variable local dentro función anidada: {var_local}')
    
  funcion_anidada()
  
imprimir()
print(f'var global fuera de la función: {var_global}')



  