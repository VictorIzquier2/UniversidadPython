
numeros = [1,2,3]

# Desempaquetando al momento de pasar un parámetro a una función
def sumar(a,b,c):
  print(f'resultado: {a + b + c}')
  
sumar(*numeros)

