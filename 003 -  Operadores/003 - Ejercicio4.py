#Par o Impar

def paresNones():
  entrada: int = int(input("Por favor, ingrese un número: "))
  if(entrada % 2 == 0):
    print(f"{entrada} es un número par")
  else:
    print(f"{entrada} es un número impar")

paresNones()
  