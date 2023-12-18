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



