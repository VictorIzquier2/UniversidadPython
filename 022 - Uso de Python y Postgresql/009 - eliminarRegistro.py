import psycopg2

conexion = psycopg2.connect(
  user='postgres', 
  password='admin', 
  host='127.0.0.1',
  port= '5434',
  database='test_db'
  )

try:
  with conexion as conn:
    with conn.cursor() as cursor:
      sentencia = 'DELETE FROM persona WHERE id_persona=%s'
      entrada = input('Proporciona el id_persona a eliminar: ')
      valores = (entrada,)
      cursor.execute(sentencia, valores)
      registros_eliminados = cursor.rowcount
      print(f'registros eliminados: {registros_eliminados}')
except Exception as e:
  print(F'Ocurrió un error: {e}, {type(e)}')
finally:    
  conexion.close()