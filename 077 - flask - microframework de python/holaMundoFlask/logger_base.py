import logging

class CustomFormatter(logging.Formatter):
    '''Custom Formatter to add emojis based on log level'''

    # Definimos los emojis
    EMOJIS = {
        logging.DEBUG: "🐛",
        logging.INFO: "🌐",
        logging.WARNING: "🚨",
        logging.ERROR: "❌",
        logging.CRITICAL: "🚫"
    }

    def format(self, record):
        # Modifica el mensaje para incluir el emoticono según el nivel de log
        record.msg = f"{self.EMOJIS.get(record.levelno, '')} {record.msg}"
        return super().format(record)

def log(app, logging_level):
    # Eliminar los handlers preexistentes
    del app.logger.handlers[:]

    # Configurar el logger
    handler = logging.StreamHandler()
    formatter = CustomFormatter('[%(asctime)s, %(lineno)d] %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    # Ajustar el nivel del logger a DEBUG para capturar todos los mensajes
    if logging_level == 'DEBUG':
      app.logger.setLevel(logging.DEBUG)
    elif logging_level == 'INFO':
      app.logger.setLevel(logging.INFO)
    elif logging_level == 'WARNING':
      app.logger.setLevel(logging.WARNING)
    elif logging_level == 'ERROR':
      app.logger.setLevel(logging.ERROR)
    elif logging_level == 'CRITICAL':
      app.logger.setLevel(logging.CRITICAL)

    # Detener la propagación de los loggers anteriores
    app.logger.propagate = False
