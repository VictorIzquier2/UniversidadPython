# GUI - Graphical User Interface
# Tkinter TK Interface
# Importar el módulo de tkinter

import tkinter as tk

# Creamos un objeto usando la clase tk
ventana = tk.Tk()

# Modificar el tamaño de la ventana (pixeles)
ventana.geometry('640x420')

# Cambiamos el nombre de la ventana
ventana.title('Nueva Ventana')

# Configuramos el icono de la aplicacion
ventana.iconbitmap('icono.ico')

# Iniciar la ventana (esta linea se ejecuta al final para que se muestre la ventana)
# Si se ejecuta antes, no se muestran los cambios anteriores
ventana.mainloop()




