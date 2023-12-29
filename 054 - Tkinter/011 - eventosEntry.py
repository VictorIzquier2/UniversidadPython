import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('640x420')
ventana.title('Manejo de Grid')
ventana.iconbitmap('icono.ico')

#entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, show='*')
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.NORMAL)
entrada1.grid(row=0, column=0)

entrada1.insert(0, 'Introduce una cadena')
entrada1.insert(tk.END, ':')

#entrada1.config(state='readonly')

# Evento
def enviar():
  print(entrada1.get())
  boton1.config(text=entrada1.get())
  # Eliminar el contenido
  # entrada1.delete(0, tk.END)
  # Seleccionar el texto de la caja
  entrada1.select_range(0, tk.END)
  # Para hacer efectiva la selección del texto
  entrada1.focus()
  

# Creamos un boton
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)
ventana.mainloop()