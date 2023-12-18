# listar todas las clases y métodos de Python
# print(dir(__builtins__))
# help(zip)

numeros = [1,2,3]
letras = ['a', 'b', 'c', 'd']
identificadores = 321, 322, 323, 324, 325
conjunto = {6, 4, 0, 9, 8, 15, 10}
mezcla = zip(numeros, letras)
#print(mezcla)
#print(list(mezcla))
#print(tuple(zip(numeros, letras)))
#print(type(mezcla))

mezcla = zip (numeros, letras, identificadores, conjunto)
print(tuple(mezcla))

for numero, letra, id, aleatorio in zip(numeros, letras, identificadores, conjunto):
  print(f'Numero: {numero}, Letra: {letra}, Identificador: {id}, Aleatorio: {aleatorio}')
  
nueva_lista = []
for numero, letra, id, aleatorio in zip(numeros, letras, identificadores, conjunto):
  nueva_lista.append(f'{id}-{numero}-{letra}-{aleatorio}')
print(nueva_lista)