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
      sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
      id_persona = input('Proporciona el valor id_persona: ')
      cursor.execute(sentencia, (id_persona,))
      registros = cursor.fetchone()
      print(registros)
except Exception as e:
  print(F'Ocurrió un error: {e}, {type(e)}')
finally:    
  conexion.close()