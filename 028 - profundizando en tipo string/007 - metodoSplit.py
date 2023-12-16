# Profundizando en el tipo str

# help(str.split)

cursos = 'Java Python JavaScript Angular Spring Excel'
lista_cursos = cursos.split()
print(f'Lista cursos: {lista_cursos}')
print(type(lista_cursos))

cursos_separados_coma = 'Java, Python, JavaScript, Angular, Spring, Excel'
lista_cursos = cursos_separados_coma.split(', ')
print(f'lista cursos: {lista_cursos}')
print(len(lista_cursos))

lista_cursos = cursos_separados_coma.split(', ', 2)
print(f'lista cursos: {lista_cursos}')
print(len(lista_cursos))
