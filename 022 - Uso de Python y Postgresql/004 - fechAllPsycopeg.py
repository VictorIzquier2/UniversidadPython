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
      sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
      # llaves_primarias = ((1,2),)
      entrada = input('Proporciona los id\'s a buscar (separado por comas): ')
      llaves_primarias = (tuple(entrada.split(',')),)
      cursor.execute(sentencia, llaves_primarias)
      registros = cursor.fetchall()
      for registro in registros:
        print(registro)
except Exception as e:
  print(F'Ocurrió un error: {e}, {type(e)}')
finally:    
  conexion.close()