# Tuplas en Python

frutas: tuple = ('Naranja', 'Plátano', 'Guayaba')

print(frutas)

print(len(frutas))

print(frutas[1])

print(frutas[-1])

print(frutas[0:1])

for fruta in frutas:
  print(fruta, end=' ')

#Convertir a una lista
frutasL : list = list(frutas)
frutasL[0] = 'Pera'
#Reconvertir a una tupla
frutas = tuple(frutasL)
print(frutas)

del frutas
try:
  frutas : print(frutas)
except:
  print("Frutas no existe")
  