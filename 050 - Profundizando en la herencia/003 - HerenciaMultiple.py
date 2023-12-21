# Ejemplo de herencia simple

class ListaSimple:
  def __init__(self, elementos):
    self._elementos = list(elementos)
    
  def agregar(self, elemento):
    self._elementos.append(elemento)
    
  def __getitem__(self, indice):
    return self._elementos[indice]
  
  def ordenar(self):
    self._elementos.sort()
    
  def __len__(self):
    return len(self._elementos)
  
  def __repr__(self):
    return f'{self.__class__.__name__}({self._elementos})'
  
class ListaOrdenada(ListaSimple):
  def __init__(self, elementos=[]):
    super().__init__(elementos)
    # Ordenamos siempre los elementos una vez inicializados
    self.ordenar()
    
  def agregar(self, elemento):
    super().agregar(elemento)
    # Ordenamos el nuevo elemento
    self.ordenar()
    
class ListaEnteros(ListaSimple):
  def __init__(self, elementos = []):
    for elemento in elementos:
      self._validar(elemento)
    # Una vez validados los elementos, los agregamos
    super().__init__(elementos)
    
class ListaEnterosOrdenada(ListaEnteros, ListaOrdenada):
  pass
  
    
  def _validar(self, elemento):
    # Validamos si el elemento es de tipo entero
    if not isinstance(elemento, int):
      raise ValueError(f'No es un valor entero: {elemento}')
    
  # sobrescribimos el método agregar de la clase padre
  def agregar(self, elemento):
    self._validar(elemento)
    # Una vez validado lo agregamos a la lista
    super().agregar(elemento)
      
# Lista simple      
lista_simple = ListaSimple([5,3,6,8])
print(lista_simple)

# Lista ordenada
lista_ordenada = ListaOrdenada([5,3,6,4])
print(lista_ordenada)
lista_ordenada.agregar(1)
print(lista_ordenada)
print(len(lista_ordenada))

# Lista enteros
#lista_enteros = ListaEnteros(['hola', 1, 3, 4])
#print(lista_enteros)

#Lista enteros ordenada
lista_enteros_ordenada = ListaEnterosOrdenada([4,5, -1, 1, 14, -4])
print(lista_enteros_ordenada)
lista_enteros_ordenada.agregar(-20)
print(lista_enteros_ordenada)
#lista_enteros_ordenada.agregar('Hola')

# Saber las clases padre y su orden
print(ListaEnterosOrdenada.__bases__)

# MRO (Method resolution order)
print(ListaEnterosOrdenada.__mro__)
