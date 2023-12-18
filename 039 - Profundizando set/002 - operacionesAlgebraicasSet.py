

# Operaciones de conjuntos con set
# Personas con distintas características
pelo_negro = {'Juan', 'Karla', 'Pedro', 'María'}
pelo_rubio = {'Lorenzo', 'Laura', 'Marco'}
ojos_cafe = {'Karla', 'Laura'}
menores_30 = {'Juan', 'Karla', 'María'}

# Todos con ojos_Cafe y pelo rubio (Union) (No se repiten elementos)
print(ojos_cafe.union(pelo_rubio))

# Invertir el orden con el mismo resultado (conmutativa)
print(pelo_rubio.union(ojos_cafe))

# (Intersection) Sólo las personas con ojos café y pelo rubio
print(ojos_cafe.intersection(pelo_rubio))

# (Difference) Pelo negro sin ojos cafe
print(pelo_negro.difference(ojos_cafe))

# (diferencia simétrica) pelo negro o ojos café pero no ambos
print(pelo_negro.symmetric_difference(ojos_cafe))
