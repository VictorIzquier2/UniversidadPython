from logger_base import log
from UsuarioDAO import UsuarioDAO
from Usuario import Usuario

opcion = None

while(opcion is not 5):
  print('Opciones:')
  print('1. Listar usuarios')
  print('2. Agregar usuario')
  print('3. Modificar usuario')
  print('4. Eliminar usuario')
  print('5. Salir')
  try:
    opcion = int(input('Escribe tu opción(1-5): '))
    if opcion == 1:
      usuarios = UsuarioDAO.seleccionar()
      for usuario in usuarios:
        log.info(usuario)
    elif opcion == 2:
      try:
        username_var = input('Introduce el nombre de usuario: ')
        password_var = input('Introduce la contraseña: ')
        usuario = Usuario(username=username_var, password=password_var)
        usuario_insertado = UsuarioDAO.insertar(usuario)
        log.info(f'Usuario insertado: {usuario_insertado}')
      except Exception as e:
        log.error(f'Ocurrió un error: {e}, {type(e)}')
    elif opcion == 3:
      try:
        id_usuario_var = int(input('Introduce el id de usuario: '))
        username_var = input('Introduce el nombre de usuario: ')
        password_var = input('Introduce la contraseña: ')
        usuario = Usuario(username=username_var, password=password_var, id_usuario=id_usuario_var)
        usuario_actualizado = UsuarioDAO.actualizar(usuario)
        log.info(f'Usuario actualizado: {usuario_actualizado}')
      except Exception as e:
        log.error(f'Ocurrió un error: {e}, {type(e)}')
    elif opcion == 4:
      try:
        id_usuario_var = int(input('Introduce el id de usuario: '))
        usuario = Usuario(id_usuario=id_usuario_var)
        usuario_eliminado = UsuarioDAO.eliminar(usuario)
        log.info(f'Usuario eliminado: {usuario_eliminado}')
      except Exception as e:
        log.error(f'Ocurrió un error: {e}, {type(e)}')
  except Exception as e:
    log.error(f'Ocurrió un error: {e}', {type(e)})
else:
  log.info('Fin de la aplicación.')
    