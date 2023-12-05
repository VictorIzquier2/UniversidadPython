def multiplicar(*args):
  producto = 1
  for multiplicando in args:
    producto *= multiplicando
  return producto

print(multiplicar(3,5,2))