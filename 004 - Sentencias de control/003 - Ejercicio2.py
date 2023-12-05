# Escoger una estaciondel año

mes = int(input('Introduce mes del año (1-12)'))
estacion = None

if mes == 1 or 2 or 12:
  estacion = 'Invierno'
elif mes == 3 or 4 or 5:
  estacion = 'Primavera'
elif mes == 6 or 7 or 8:
  estacion = 'Verano'
elif mes == 9 or 10 or 11:
  estacion = 'Otoño'
else:
  estacion = 'Mes incorrecto'
print(f'Para el mes {mes} la estación es: {estacion}')