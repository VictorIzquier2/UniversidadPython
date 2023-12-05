# Diccionarios
# Como un diccionario tiene una llave y un valor

diccionario = {
  'IDE': 'Integrated Development Environment',
  'OOP': 'Object Oriented Programming',
  'DBMS': 'Database Management System'
}

print(diccionario)

print(len(diccionario))

print(diccionario['IDE']) #key

print(diccionario.get('OOP')) #key

diccionario['IDE'] = 'integrated development environment'
print(diccionario)

for termino, valor in diccionario.items():
  print(termino, valor)
  
for termino in diccionario.keys():
  print(termino)
  
for valor in diccionario.values():
  print(valor)
  
diccionario['PK'] = 'Primary Key'
print(diccionario)

diccionario.pop('DBMS')
print(diccionario)

diccionario.clear()
print(diccionario
      )

