def imprimir(numero):
  if numero == 1:
    print(1)
  else:
    print(numero)
    return imprimir(numero-1)
  
  
imprimir(7)
