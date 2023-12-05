
def accesoEdad(edadAdulta: int):
  edad: int = int(input("Dime tu edad: "))
  if edad >= edadAdulta:
    print(f'La persona con edad {edad} tiene acceso permitido.')
  else:
    print(f'La persona con edad {edad} tiene acceso denegado.')
    
accesoEdad(18)