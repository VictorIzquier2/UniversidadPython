import psycopg2 as bd

conexion = bd.connect(
  user='postgres', 
  password='admin', 
  host='127.0.0.1',
  port= '5434',
  database='test_db'
  )

try:
  with conexion as conn:
    with conn.cursor() as cursor:
      
      sentencia = 'insert INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
      valores = ('Alex', 'Rojas', 'arojas@mail.com')
      cursor.execute(sentencia, valores)
      
      sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
      valores = ('Juan','Perez', 'jperez@mail.com', 1)
      cursor.execute(sentencia, valores)
      
      '''
      sentencia = 'DELETE FROM persona WHERE id_persona=%s'
      id_persona = 9
      valores = (id_persona,)
      cursor.execute(sentencia, valores)
      '''
  
      conn.commit()
except Exception as e:
  print(F'Ocurrió un error: {e}, {type(e)}')
finally:    
  conexion.close()
  print('Termina la transacción, se hizo commit')