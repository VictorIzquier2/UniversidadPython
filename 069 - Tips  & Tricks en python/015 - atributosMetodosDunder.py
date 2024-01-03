# dunder = Double underscore

class Padre:
  def __init__(self):
    # Al usar dunder (double underscore) al inicio y al final
    # No se aplica el concepto de name mangling
    self.__variable_dunder__ = 10

if __name__ == '__main__':
  padre = Padre()
  print(dir(padre))
  print(f'Accediendo a la variable dunder: {padre.__variable_dunder__}')