

mensaje = b'Universidad Python'
print(mensaje[1])
print(chr(mensaje[1]))

lista_caracteres = mensaje.split()
print(lista_caracteres)

# Convertir str a bytes
string = 'Programación con Python'
print('String original:', string)
bytes = string.encode('UTF-8')
print('bytes codificado:', bytes)

# Convertir de bytes a string
string2 = bytes.decode('UTF-8')
print(string2)