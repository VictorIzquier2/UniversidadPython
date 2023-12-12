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
      sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
      valores = (
        ('Juan', 'Pérez', 'jperez@mail.com', 1),
        ('Ivonne', 'Gutiérrez', 'igutierrez@mail.com', 2)
        )
      cursor.executemany(sentencia, valores)
      registros_actualizados = cursor.rowcount
      print(f'registros actualizados: {registros_actualizados}')
except Exception as e:
  print(F'Ocurrió un error: {e}, {type(e)}')
finally:    
  conexion.close()