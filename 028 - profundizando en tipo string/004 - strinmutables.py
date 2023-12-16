
mensaje1 = 'hola mundo'
mensaje2 = mensaje1.capitalize()

print(f'mensaje1: {mensaje1}, id: {hex(id(mensaje1))}')
print(f'mensaje2: {mensaje2} id: {hex(id(mensaje2))}')

mensaje1 += 'adios'
print(f'mensaje1: {mensaje1}, id: {hex(id(mensaje1))}') # Cualquier modificación en un objeto string crea una nueva direccion de memoria. Son inmutables

