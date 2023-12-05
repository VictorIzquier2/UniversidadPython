# Set

planetas = {'Mercurio', 'Venus', 'La Tierra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Neptuno'}

# Los elementos no están ordenados
print(planetas)

print(len(planetas))

# Revisar si un elemento está presente
print('Marte' in planetas)

planetas.add('Plutón')
print(planetas)

planetas.remove('Plutón')
print(planetas)

# Elimina elementos sin arrojar errores en caso de que no se encuentre
planetas.discard('Júpiters')
print(planetas)

planetas.clear()
print(planetas)

del planetas
try:
  print(planetas)
except:
  print('No se encontró el set')

