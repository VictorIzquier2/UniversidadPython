# Dada la siguiente tupla,
# crear una lista que solo incluya los número menores a 5

tupla = (13, 1, 8, 3, 2, 5, 8)

lista = []

for num in tupla:
  if num < 5:
    lista.append(num)
else:
  print(lista)
