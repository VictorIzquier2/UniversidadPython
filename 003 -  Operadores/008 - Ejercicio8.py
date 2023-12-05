# Tienda de libros


def pedidoLibro():
  print("Proporciona los siguientes datos de un libro:\n")
  nombre: str = input("Introduce el nombre: ")
  id: int = int(input("Introduce el ID: "))
  precio: float = float(input("Introduce el precio: "))
  envio: bool = bool(input("Indica si el envío es gratuito (True/False): "))
  
  print(f"\nNombre: {nombre}\nId: {id}\nPrecio: {precio}\nEnvío gratuito: {envio}\n")
  
pedidoLibro()