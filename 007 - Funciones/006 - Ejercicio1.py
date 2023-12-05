def sumar(*args):
  sumatorio: int = 0
  for suma in args:
    sumatorio+=suma
  return sumatorio

print(sumar(1,2,3,4,5))