##########################################
# Decoradores con argumentos
# *args, **kwargs

def decorador_con_argumentos(funcion):
  def funcion_envolvente(*args, **kwargs):
    print('args', args)
    print('kwargs', kwargs)
    # Modificar los argumentos antes de enviarlos
    lista_arg = []
    for indice, valor_tupla in enumerate(args):
      lista_arg.append(args[indice].upper())
    # Agregamos más elementos a la lista
    lista_arg.append('nuevo arg 1')
    lista_arg.append('nuevo arg 2')
    # Agregamos información al diccionario
    kwargs['valor1'] = 'Nuevo valor 1'
    kwargs['valor2'] = 'Nuevo valor 2'
    # Propagamos los parametros a la funcion original
    #return funcion(*args, **kwargs)
    # Propagar los valores modificados
    return funcion(*lista_arg, **kwargs)
  return funcion_envolvente

@decorador_con_argumentos
def funcion_saludar(titulo, nombre, *args, **kwargs):
  # Imprimir título con el nombre
  print(f'{titulo}. {nombre}')
  # Imprimimos los argumentos variables
  print('args:', args)
  print('kwargs:', kwargs)
  
funcion_saludar('Ingeniera', 'María Quiroz')