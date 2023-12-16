# 


mensaje = 'Hola Mundo'
print(mensaje.lower().islower())

# alinear cadenas

# center - Centrar un str
titulo = 'Sitio Web de GlobalMentoring.com.mx'
print(titulo.center(50,'*'))
print(len(titulo.center(50, '*')))
print(titulo.center(len(titulo)+10, '-'))

print(titulo.ljust(50, '*'))