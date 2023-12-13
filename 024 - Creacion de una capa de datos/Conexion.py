import psycopg2 as bd
import sys
from logger_base import log

class Conexion:
  _DATABASE = 'test_db'
  _USERNAME = 'postgres'
  _PASSWORD = 'admin'
  _DB_PORT = '5434'
  _HOST = '127.0.0.1'
  _conexion = None
  _cursor = None
  
  @classmethod
  def obtenerConexion(cls):
    if cls._conexion is None:
      try:
        cls._conexion = bd.connect(user=cls._USERNAME, password=cls._PASSWORD, host=cls._HOST, port=cls._DB_PORT, database=cls._DATABASE)
        log.debug(f'Conexión realizada con éxito: {cls._conexion}')
        return cls._conexion
      except Exception as e:
        log.error(f'Ocurrió una excepción durante la conexión: {e}, {type(e)}')
        sys.exit()
    else:
      return cls._conexion
  
  @classmethod
  def obtenerCursor(cls):
    if cls._cursor is None:
      try:
        cls._cursor = cls.obtenerConexion().cursor()
        log.debug(f'Se abrió correctamente el cursor: {cls._cursor}')
        return cls._cursor
      except Exception as e:
        log.error(f'Ocurrió una excepción al obtener el cursor: {e}, {type(e)}')
        sys.exit()
    else:
      return cls._cursor
  
if __name__ == '__main__':
  Conexion.obtenerConexion()
  Conexion.obtenerCursor()
  