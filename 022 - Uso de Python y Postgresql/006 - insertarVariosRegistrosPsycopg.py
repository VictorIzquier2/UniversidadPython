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
      sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s,%s, %s)'
      valores = (
        ('Marcos', 'Cantu', 'mcantu@mail.com'),
        ('Angel', 'Quintana', 'aquintana@mail.com'),
        ('Maria', 'Gonzalez', 'mgonzalez@mail.com')
        )
      cursor.executemany(sentencia, valores)
      #conexion.commit()
      registros_insertados = cursor.rowcount
      print(f'registros insertados: {registros_insertados}')
except Exception as e:
  print(F'Ocurrió un error: {e}, {type(e)}')
finally:    
  conexion.close()