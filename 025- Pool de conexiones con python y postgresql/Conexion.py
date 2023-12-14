from psycopg2 import pool
import sys
from logger_base import log

class Conexion:
  _DATABASE = 'test_db'
  _USERNAME = 'postgres'
  _PASSWORD = 'admin'
  _DB_PORT = '5434'
  _HOST = '127.0.0.1'
  _MIN_CON = 1
  _MAX_CON = 5
  _pool = None
  
  @classmethod
  def obtenerPool(cls):
    if cls._pool is None:
      try:
        cls._pool = pool.SimpleConnectionPool(
          cls._MIN_CON, 
          cls._MAX_CON, 
          host=cls._HOST, 
          user=cls._USERNAME, 
          password=cls._PASSWORD, 
          port=cls._DB_PORT, 
          database=cls._DATABASE)
        log.debug(f'El pool se creó correctamente: {cls._pool}')
        return cls._pool
      except Exception as e:
        log.error(f'Ocurrió un error al obtener el pool: {e}, {type(e)}')
        sys.exit()
    else:
      return cls._pool
  
  @classmethod
  def obtenerConexion(cls):
    conexion = cls.obtenerPool().getconn()
    log.debug(f'Conexion obtenida del pool: {conexion}')
    return conexion
    
  @classmethod
  def liberarConexion(cls, conexion):
    cls.obtenerPool().putconn(conexion)
    log.debug(f'Conexión regresada al pool: {conexion}')
    
  @classmethod
  def cerrarConexiones(cls):
    cls.obtenerPool().closeall()
    log.debug(f'Todas las conexiones fueron cerradas: {cls._pool.closed}')
    
if __name__ == '__main__':
  conexion1 = Conexion.obtenerConexion()
  Conexion.liberarConexion(conexion1)
  conexion2 = Conexion.obtenerConexion()
  Conexion.cerrarConexiones()
  
  