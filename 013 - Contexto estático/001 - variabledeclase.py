class MiClase:
  variable_clase = 'Valor variable clase'
  
  def __init__(self, variable_instancia):
    self.variable_instancia = variable_instancia
    
    
print(MiClase.variable_clase)

miClase = MiClase('valor variable instancia')
print(miClase.variable_instancia)

miClase2 = MiClase('Otro valor de variable instancia')
print(miClase2.variable_clase)
print(miClase2.variable_instancia)