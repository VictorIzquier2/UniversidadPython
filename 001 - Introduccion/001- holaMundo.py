x = 10

def print_hi(name):
  print(f'Hi, {name}')
  
if __name__ == '__main__':
  print_hi('PyCharm')
  # Dirección de memoria
  print_hi(id(x))
  