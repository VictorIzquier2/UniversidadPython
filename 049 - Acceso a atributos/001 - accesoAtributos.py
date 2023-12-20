# Ejemplo atributos públicos, protegidos, privados

class Miclase:
  def __init__(self, publico, protegido, privado):
    self.publico = publico
    self._protegido = protegido
    self.__privado = privado
    
objeto = Miclase('Valor público', 'Valor protegido', 'Valor privado')

# Acceso al atributo público
print(objeto.publico)

# Modificar el valor público
objeto.publico = 'Nuevo valor público'
print(objeto.publico)

# Acceso al valor protegido
# solo dentro de la misma clase o clases hijas
print(objeto._protegido)

# Modificar atributo protegido
objeto._protegido = 'Nuevo valor protegido'
print(objeto._protegido)

# Acceder al valor privado
# print(objeto.__privado) No se puede acceder directamente
# Pero, convierte: objeto._clase__atributo_privado
objeto._Miclase__privado = 'Nuevo valor privado'
print(objeto._Miclase__privado) # No es recomendable


       
  