

mensaje = 'Hola Mundo'
print(mensaje.lower().islower())

# alinear cadenas

# center - Centrar un str
titulo = 'Sitio Web de GlobalMentoring.com.mx'
print(titulo.ljust(50, '*'))

titulo = 'Sitio Web de GlobalMentoring.com.mx'
print(titulo.rjust(50, '*'))
print(titulo.rjust(len(titulo)+10, '-'))