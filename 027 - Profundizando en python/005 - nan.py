import math
from decimal import Decimal
# Not a Number (representa un valor numérico indefinido)

# float
a = float('NaN')
print(f'a: {a}')
print(f'Es NaN (not a number)?: {math.isnan(a)}')

# decimal
a = Decimal('NaN')
print(f'a: {a}')
print(f'Es NaN (not a number)?: {math.isnan(a)}')
