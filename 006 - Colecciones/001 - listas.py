# Listas en Python

nombres : list = ['Juan', 'Karla', 'Ricardo', 'Maria']

for nombre in nombres:
  print(nombre)
else:
  print('No existen más nombres en la lista')

#print(nombres[0])
#print(nombres[0:2]) # Sin incluir el índice 2 
#print(nombres[:3]) # desde el inicio hasta el índice 3 sin incluir
#print(nombres[1:]) # desde el índice 1 incluido hasta el final
print(len(nombres))

#Agregar un nombre a la lista
nombres.append('Lorenzo')
print(nombres)

#insertar un nombre en un índice específico
nombres.insert(1, 'Octavio')
print(nombres)

nombres.remove('Octavio')
print(nombres)

#Eliminar el último de la lista
nombres.pop()
print((nombres))

#Eliminar un índice
del nombres[0]
print(nombres)




