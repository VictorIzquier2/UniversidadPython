class Usuario:
  def __init__(self, id_usuario=None, username=None, password=None):
    self.id_usuario = id_usuario
    self.username = username
    self.password = password
    
  def __str__(self):
    return f'Usuario id: {self.id_usuario} [ Nombre de usuario: {self.username}, Password: {self.password} ]'