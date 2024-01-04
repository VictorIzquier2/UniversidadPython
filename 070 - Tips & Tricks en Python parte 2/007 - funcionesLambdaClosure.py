# Las funciones lambda también podemos aplicar el concepto de closure
def mostrar(titulo):
  return lambda mensaje: titulo + '. ' + mensaje

mostrar_ing = mostrar('Ingeniero')
mostrar_lic = mostrar('Licenciado')
print(mostrar_ing('Carlos Lara'))
print(mostrar_lic('Armando Casas'))
