from orden import Orden
from computadora import Computadora
from monitor import Monitor
from teclado import Teclado
from raton import Raton

# Monitores
monitor1 = Monitor('HP', 15)
monitor2 = Monitor('Acer', 27)

# Teclados
teclado1 = Teclado('HP', 'USB')
teclado2 = Teclado('Gamer', 'Bluetooth')

# Ratones
raton1 = Raton('HP', 'USB')
raton2 = Raton('Acer', 'Bluetooth')

# Computadoras
computadora1 = Computadora('HP', monitor1, teclado1, raton1)
computadora2 = Computadora('Acer', monitor2, teclado2, raton2)

# Orden
orden1 = Orden([computadora1, computadora2])
print(orden1)


