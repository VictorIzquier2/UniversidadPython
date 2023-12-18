# Preguntas sobre Conjuntos

# El conjunto B está dentro del conjunto A?
# El conjunto A contiene a todo el conjunto B?
# El conjunto A no tiene relación con el conjunto B?

pelo_negro = {'Juan', 'Karla', 'Pedro', 'María'}
pelo_rubio = {'Lorenzo', 'Laura', 'Marco'}
ojos_cafe = {'Karla', 'Laura'}
menores_30 = {'Juan', 'Karla', 'María'}

# Preguntar si un set está contenido en otro (subset)
# revisar si los elementos del primer set están contenidos en el segundo from django.conf import settings
print(menores_30.issubset(pelo_negro)) # Todos los menores de 30 tienen el pelo negro

# Preguntar si un set contiene a otro set (superset)
# revisar si los elementos del primer set están contenidos en el segundo from django.conf import settings
print(pelo_negro.issuperset(menores_30)) # Todos los menores de 30 tienen el pelo negro

# Preguntar si los de pelo negro no tienen el pelo rubio (disjoin)
print(pelo_negro.isdisjoint(pelo_rubio)) # Ninguna persona tiene el pelo rubio y negro al mismo tiempo
