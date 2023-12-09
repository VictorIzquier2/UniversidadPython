class MiClase:
  variable_clase = 'Valor variable clase'
  
  def __init__(self, variable_instancia):
    self.variable_instancia = variable_instancia
    
    
print(MiClase.variable_clase)

miClase = MiClase('valor variable instancia')
print(miClase.variable_instancia)

miClase.variable_clase2 = 'valor variable clase 2'
print(miClase.variable_clase2)