

contenido = 'Sitio Web de GlobalMentoring.com.mx'
print(contenido.replace(' ', '-'))


# Eliminar caracters al inicio y al final de un str - strip
titulo = ' *** GlobalMentoring.com.mx *** '
print(f'Cadena origina: {titulo} {len(titulo)}')
titulo = titulo.strip()
print('Cadena modificada:', titulo, len(titulo))
titulo = titulo.strip('*')
print(f'Cadena modificada sin *: {titulo} {len(titulo)}')
titulo = titulo.strip()
print(f'Cadena modificada sin otros espacios: {titulo} {len(titulo)}')
