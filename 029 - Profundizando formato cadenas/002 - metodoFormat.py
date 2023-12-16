# Profundizando en el tipo str

# Dar formato a un str

nombre = 'Juan'
edad = 28
sueldo = 3000
mensaje_con_formato = 'Nombre {} Edad {} Sueldo {:.2f}€'.format(nombre, edad, sueldo)
print(mensaje_con_formato)

mensaje = 'Nombre {0} Edad {1} Sueldo {2:.2f}€'.format(nombre, edad, sueldo)
print(mensaje)

mensaje = 'Nombre {n} Edad {e} Sueldo {s:.2f}€'.format(n=nombre, e=edad, s=sueldo)
print(mensaje)

diccionario = {'nombre': 'Ivan', 'edad':35, 'sueldo':8000.00}
mensaje = 'Nombre: {persona[nombre]:s} Edad: {persona[edad]:d} Sueldo {persona[sueldo]:.2f}'.format(persona=diccionario)
print(mensaje)