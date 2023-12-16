# Leer contenido online

from urllib.request import Request, urlopen
 
request = Request("https://www.globalmentoring.com.mx/recursos/GlobalMentoring.txt") 
request.add_header(
  'User-Agent', 
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
  )

palabras = []
with urlopen(request) as response:
    for linea in response:
      palabras_por_linea = linea.decode('utf-8').split()
      print(palabras_por_linea)
      for palabra in palabras_por_linea:
        palabras.append(palabra)
print(palabras)