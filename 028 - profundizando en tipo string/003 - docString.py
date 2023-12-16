'''
Comentario
varias lineas
'''


class MiClase:
  '''
  Este es un ejemplo de la documentación de clase
  '''
  
  def __init__(self):
    '''
    Método de inicio de nuestra clase
    '''
    
  def mi_metodo(self, param1, param2):
    '''
    Esta es la documentación de nuestro método
    :param param1 Este es el parámetro 1:
    :param param2 Este es el parámetro 2:
    :return Este es el valor de retorno:
    '''
    
# help(MiClase)

# print(MiClase.__doc__)
print(MiClase.mi_metodo.__doc__)
print(type(MiClase.mi_metodo))