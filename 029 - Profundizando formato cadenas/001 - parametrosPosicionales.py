# Profundizando en el tipo str

# Dar formato a un str

nombre = 'Juan'
edad = 28
mensaje_con_formato = 'Mi nombre es %s y tengo %d años'%(nombre, edad)
print(mensaje_con_formato)

persona = ('Karla', 'Gómez', 5000)
mensaje_con_formato = 'Hola %s %s. Tu sueldo es de %.2f€'%persona
print(mensaje_con_formato)
