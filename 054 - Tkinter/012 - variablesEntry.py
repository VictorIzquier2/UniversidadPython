import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('640x420')
ventana.title('Manejo de Grid')
ventana.iconbitmap('icono.ico')

# Definimos una variable que podremos modificar posteriormente (set), leer(get)
entrada_var1 = tk.StringVar(value='Valor por default')
entrada1 = ttk.Entry(ventana, width=30, textvariable=entrada_var1)
entrada1.grid(row=0, column=0)
#entrada1.insert(0, 'Introduce una cadena')
#entrada1.insert(tk.END, ':')

#entrada1.config(state='readonly')

# Evento
def enviar():
  # Recuperamos la información a partir de la variable asociada con la caja de texto
  boton1.config(text=entrada_var1.get())
  # Modificación utilizamos la variable de texto y el método set
  entrada_var1.set('Cambió...')
  # Recuperamos la información
  print(entrada_var1.get())
  print(entrada1.get())

# Creamos un boton
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)
ventana.mainloop()