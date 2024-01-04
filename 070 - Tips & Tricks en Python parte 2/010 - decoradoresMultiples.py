##########################################

# Decoradores múltiples
# <strong><em>Hola</em></strong>

def negritas(funcion):
  def funcion_envolvente():
    return '<strong>' + funcion() + '</strong>'
  return funcion_envolvente

def enfatizar(funcion):
  def funcion_envolvente():
    return '<em>' + funcion() + '</em>'
  return funcion_envolvente

@negritas
@enfatizar
def saludar_html():
  return 'Hola con HTML'

print(saludar_html())

