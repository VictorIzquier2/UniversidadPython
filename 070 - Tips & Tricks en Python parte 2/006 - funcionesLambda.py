# Las funciones lambda nos permiten declarar funciones anónimas
# en una sola línea de código
# Ejemplo normal

def sumar(a, b):
  return a + b

print(sumar(3,5))

# Función lambda
sumar_lamda = lambda a, b: a + b
print(sumar_lamda(2,4))

# Utilizando una sola línea de código
print((lambda a, b: a + b)(5,6))

# Podemos usar una función lambda siempre que necesitemos una función concreta
# Ej. Ordenar una lista de tuplas, por su segundo valor proporcionado una llave
lista_tuplas = [(1, 'b'), (2, 'f'), (5, 'a'), (4, 'c')]
lista_tuplas_ordenada = sorted(lista_tuplas, key=lambda tupla: tupla[0])
print(lista_tuplas_ordenada)

# Otro ejemplo de ordenamiento usando una expresión lambda
print(list(range(-3,4)))

# Si queremos ordenar por el valor absoluto (sin considerar signo)
for valor in range(-3, 4):
  print(valor, valor*valor)
  
  # aplicamos expresión lambda
  lista_ordenada = sorted(range(-3,4), key=lambda valor: valor*valor)
  print(lista_ordenada
        )