import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.geometry('640x420')
ventana.title('Manejo de Grid')
ventana.iconbitmap('icono.ico')


entrada1 = ttk.Entry(ventana, width=30)
entrada1.grid(row=0, column=0)

# Etiqueta (label)
etiqueta1 = tk.Label(ventana, text='Aquí se mostrará el contenido de la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)

# Evento
def enviar():
  # Modificamos el texto del label
  etiqueta1.config(text=entrada1.get())
  # Messagebox (Caja de mensajes)
  mensaje1 = entrada1.get()
  if mensaje1:
    messagebox.showinfo('Mensaje: ', mensaje1 + ' informativo')
    messagebox.showerror('Mensaje Error', mensaje1 + ' Error')
    messagebox.showwarning('Mensaje Alerta', mensaje1 + ' Alerta')
  # Eliminar el contenido
  entrada1.delete(0, tk.END)
  # Para hacer efectiva la selección del texto
  entrada1.focus()
    

# Creamos un boton
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)
ventana.mainloop()