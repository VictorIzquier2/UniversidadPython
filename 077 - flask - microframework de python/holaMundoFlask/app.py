from flask import Flask, request, render_template, url_for, abort
from werkzeug.utils import redirect
from logger_base import log  # Importa la función de configuración

app = Flask(__name__)

log(app, 'DEBUG') # Configurar el nivel de logger para esta app

@app.route('/')
def inicio():
    app.logger.info(f'Entramos al path {request.path}')   

    return 'Hola mundo desde Flask.'
  
@app.route('/saludar/<nombre>')
def saludar(nombre):
  return f'Saludos {nombre}'

@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
  return f'Tu edad es: {edad}'

###############################################################
# PETICIONES HACIA EL SERVIDOR

@app.route('/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_nombre(nombre):
  return render_template('mostrar.html', nombre=nombre)

@app.route('/redireccionar')
def redireccionar():
  #return redirect(url_for('inicio'))
  return redirect(url_for('mostrar_nombre', nombre='Juan'))

@app.route('/salir')
def salir():
  return abort(404)

@app.errorhandler(404)
def pagina_no_encontrada(error):
  return (render_template('error404.html', error=error), 404)

###############################################################

# REST Representational state transfer
@app.route('/api/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_json(nombre):
  valores = {'nombre': nombre, 'metodo_http': request.method}
  
  return valores

if __name__=='__main__':
    app.run(debug=True)
