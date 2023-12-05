
palabra = input("Dime una palabra: ")
letra = input("Dime una letra: ")

for caracter in palabra:
  if caracter == letra:
    print(f'Letra encontrada: {letra}')
    break
else:
  print('Fin ciclo for')