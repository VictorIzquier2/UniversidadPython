from flask import Flask, request, render_template, url_for
from flask_migrate import Migrate
from werkzeug.utils import redirect
from logger_base import log
from database import db
from models import Persona
from forms import PersonaForm

app = Flask(__name__)
app.secret_key = 'Mi_llave_Secreta'
log(app, 'DEBUG') # Configurar el nivel de logger para esta app

# Configuración de la bd
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
PORT_DB = '5434'
NAME_DB = 'sap_flask_db'

FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}:{PORT_DB}/{NAME_DB}' # Cadena de conexión completa hacia postgresql

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización del objeto db de sqlalchemy
db.init_app(app)

# Configurar flask-migrate
migrate = Migrate()
migrate.init_app(app, db)

# Configurar flask-wtf
app.config['SECRET_KEY'] = app.secret_key
    
#########################################
# Rutas

# Inicio
@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
  personas = Persona.query.order_by('id')
  total_personas = Persona.query.count()
  app.logger.debug(f'Listado de Personas: {personas}')
  app.logger.debug(f'Total Personas: {total_personas}')
  return render_template('index.html', personas=personas, total_personas=total_personas)

# Ver Detalle
@app.route('/ver_detalle/<int:id>')
def ver_detalle(id):
  # Recuperamos la persona según el id proporcionado
  #persona = Persona.query.get(id) # Puede generar un error si no encuentra la persona
  persona = Persona.query.get_or_404(id)
  app.logger.debug(f'Ver detalle persona: {persona}')
  return render_template('detalle.html', persona=persona)

# Agregar Persona
@app.route('/agregar_persona', methods=['GET', 'POST'])
def agregar_persona():
  persona = Persona()
  personaForm = PersonaForm(obj=persona)
  if request.method == 'POST':
    if personaForm.validate_on_submit():
      personaForm.populate_obj(persona)
      # Insertar el registro
      db.session.add(persona)
      db.session.commit()
      app.logger.debug(f'Persona agregada: {persona}')
      return redirect(url_for('inicio')) 
  return render_template('agregar.html', forma=personaForm)

@app.route('/editar_persona/<int:id>', methods=['GET', 'POST'])
def editar_persona(id):
  # Recuperamos el objeto persona a editar
  persona = Persona.query.get_or_404(id)
  personaForm = PersonaForm(obj=persona)
  if request.method == 'POST':
    if personaForm.validate_on_submit():
      personaForm.populate_obj(persona)
      # Editar el registro
      db.session.commit()
      app.logger.debug(f'Persona editada: {persona}')
      return redirect(url_for('inicio'))
  return render_template('editar.html', forma=personaForm)

@app.route('/eliminar_persona/<int:id>', methods=['GET', 'POST'])
def eliminar_persona(id):
  persona = Persona.query.get_or_404(id)
  db.session.delete(persona)
  db.session.commit()
  app.logger.debug(f'Persona eliminada: {persona}')
  return redirect(url_for('inicio'))
  
# Pruebas
if __name__=='__main__':
    app.run(debug=True)
    
