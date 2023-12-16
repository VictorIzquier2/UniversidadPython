


lista_de_listas = [[10, 14, 87, 90, 71], [4, 5, 6, 7], [9, 0, 11, 15, 45, 61, 70]]

lista_de_listas.sort(key=len)
print(f'Ordenar lista: {lista_de_listas}')

for lista in lista_de_listas:
  lista.sort()
print(lista_de_listas)

nombres1 = ['Juan Carlos', 'Karla', 'Pedro', 'Esperanza']
nombres1 = sorted(nombres1, reverse=True)
print(nombres1)

nombres1 = sorted(nombres1, key=len)
print(nombres1)

nombres1 = reversed(nombres1)
print(list(nombres1))