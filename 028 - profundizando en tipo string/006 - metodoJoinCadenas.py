# Profundizando en el tipo str

# help(str.join)

tupla_str = ('Hola', 'Mundo', 'Universidad', 'Python')

mensaje = ' '.join(tupla_str)
print(mensaje)

lista_cursos = ['Java', 'Python', 'Angular', 'Spring']
mensaje = ', '.join(lista_cursos)
print(f'mensaje: {mensaje}')

diccionario = {'nombre':'Juan', 'apellido':'Pérez'}
mensaje = ' '.join(diccionario.values())
print(mensaje)