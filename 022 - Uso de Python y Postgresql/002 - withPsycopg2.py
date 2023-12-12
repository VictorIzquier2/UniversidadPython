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
      cursor.execute('SELECT * FROM persona')
      registros = cursor.fetchall()
      print(registros)
except Exception as e:
  print(F'Ocurrió un error: {e}, {type(e)}')
finally:    
  conexion.close()