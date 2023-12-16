# Leer contenido online

from urllib.request import Request, urlopen
 
request = Request("https://www.globalmentoring.com.mx/recursos/GlobalMentoring.txt") 
request.add_header(
  'User-Agent', 
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
  )

with urlopen(request) as response:
  contenido = response.read().decode('utf-8')
  
print('Nº de veces Universidad: ',contenido.count('Universidad'))
print(contenido.upper())
print(contenido.lower())

print('Existe python?: ','python'.lower() in contenido.lower())

print('Inicia con: ', contenido.startswith('En GlobalMentoring.com.mx'))
print('Termina con:' , contenido.endswith('GlobalMentoring.com.mx'))