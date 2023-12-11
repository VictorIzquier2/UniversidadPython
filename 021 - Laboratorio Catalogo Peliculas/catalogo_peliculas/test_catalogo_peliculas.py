from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas
opcion = None

while opcion != 4:
  print('Opciones: ')
  print('1. Agregar Pelicula')
  print('2. Listar Peliculas')
  print('3. Eliminar catálogo de peliculas')
  print('4. Salir')
  try:
    opcion = int(input('Escribe tu opción (1-4):'))
    
    if opcion == 1:
      nombre_pelicula = input('Introduce el nombre de la película: ')
      pelicula = Pelicula(nombre_pelicula)
      CatalogoPeliculas.agregar_pelicula(pelicula)
    elif opcion == 2:
      CatalogoPeliculas.listar_peliculas()
    elif opcion == 3:
      CatalogoPeliculas.eliminar_peliculas()
  except Exception as e:
    print(f'\nPor favor, elige un número del 1 al 4.\n')
    opcion = None
else:
  print('Salimos del programa...')