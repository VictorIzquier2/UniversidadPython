from CursorDelPool import CursorDelPool
from Usuario import Usuario
from logger_base import log

class UsuarioDAO:
  
  _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
  _INSERTAR = 'INSERT INTO usuario(username, password) VALUES (%s, %s)'
  _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
  _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'
  
  @classmethod
  def seleccionar(cls):
    with CursorDelPool() as cursor:
      cursor.execute(cls._SELECCIONAR)
      registros = cursor.fetchall()
      usuarios = []
      for registro in registros:
        usuario = Usuario(registro[0], registro[1], registro[2])
        usuarios.append(usuario)
      return usuarios
    
  @classmethod
  def insertar(cls, usuario):
    with CursorDelPool() as cursor:
      valores = (usuario.username, usuario.password)
      cursor.execute(cls._INSERTAR, valores)
      log.debug(f'Usuario insertado: {usuario}')
      return cursor.rowcount
  
  @classmethod  
  def actualizar(cls, usuario):
    with CursorDelPool() as cursor:
      valores = (usuario.username, usuario.password, usuario.id_usuario)
      cursor.execute(cls._ACTUALIZAR, valores)
      log.debug(f'Usuario actualizado: {usuario}')
      return cursor.rowcount
      
  @classmethod
  def eliminar(cls, usuario):
    with CursorDelPool() as cursor:
      valores = (usuario.id_usuario,)
      cursor.execute(cls._ELIMINAR, valores)
      log.debug(f'Usuario eliminado: {usuario}')
      return cursor.rowcount
    
if __name__ == '__main__':
    
  # Insertar un registro
  '''usuario1 = Usuario(username='hematocritico', password='twitter')
  usuario_insertado = UsuarioDAO.insertar(usuario1)
  log.debug(f'usuario insertado: {usuario_insertado}')'''
  
  # Actualizar un registro
  '''usuario1 = Usuario(1, 'EstoyAvisando', 'twitteresx')
  usuario_actualizado = UsuarioDAO.actualizar(usuario1)
  log.debug(f'Usuario actualizado: {usuario_actualizado}')'''

  # Eliminar un registro
  usuario1 = Usuario(id_usuario=1)
  usuario_eliminado = UsuarioDAO.eliminar(usuario1)
  log.debug(f'Usuario eliminado: {usuario_eliminado}')
  
  # Seleccionar personas
  usuarios = UsuarioDAO.seleccionar()
  for usuario in usuarios:
    log.debug(usuario)