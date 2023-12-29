# GUI - Graphical User Interface
# Tkinter TK Interface
# Importar el módulo de tkinter

import tkinter as tk
from tkinter import ttk
# En el modulo ttk están los componentes de tkinter

# Creamos un objeto usando la clase tk
ventana = tk.Tk()

# Modificar el tamaño de la ventana (pixeles)
ventana.geometry('640x420')

# Cambiamos el nombre de la ventana
ventana.title('Nueva Ventana')

# Configuramos el icono de la aplicacion
ventana.iconbitmap('icono.ico')

# Creamos un método evento_click
def evento_click():
  boton1.config(text='Botón presionado')
  print('Ejecución del evento_click')
  # Creamos un nuevo botón y lo mostramos
  boton2 = ttk.Button(ventana, text='Nuevo Botón')
  boton2.pack()

# Componentes se llaman widget
# Creamos un boton (widget), el objeto padre es ventana
boton1 = ttk.Button(ventana, text='Dar click', command=evento_click)

# Se utiliza el pack layout manager para mostrar el botón de la ventana
boton1.pack()

# Iniciar la ventana (esta linea se ejecuta al final para que se muestre la ventana)
# Si se ejecuta antes, no se muestran los cambios anteriores
ventana.mainloop()
