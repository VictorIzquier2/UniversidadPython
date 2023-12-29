import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu

ventana = tk.Tk()
ventana.geometry('640x420')
ventana.title('Manejo de Grid')
ventana.iconbitmap('icono.ico')

entrada1 = ttk.Entry(ventana, width=30)
entrada1.grid(row=0, column=0)

etiqueta1 = tk.Label(ventana, text='Aquí se mostrará el contenido de la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)

def enviar():
  etiqueta1.config(text=entrada1.get())
  mensaje1 = entrada1.get()
  if mensaje1:
    messagebox.showinfo('Mensaje: ', mensaje1 + ' informativo')
  entrada1.delete(0, tk.END)
  entrada1.focus()
  
def salir():
  ventana.quit()
  ventana.destroy()
  sys.exit()
  
def crear_menu():
  # Configurar el menú principal
  menu_principal = Menu(ventana)
  # tearoff = False para evitar que se separe el menú de la interfaz
  submenu_archivo = Menu(menu_principal, tearoff=0)
  # Agregamos una nueva opción al menú de archivo
  submenu_archivo.add_command(label='Nuevo')
  # Agregamos la opción de salir
  submenu_archivo.add_command(label='Salir', command=salir)
  # Agregamos el submenú al menú principal
  menu_principal.add_cascade(menu=submenu_archivo, label='Archivo')
  # Submenu ayuda
  submenu_ayuda = Menu(menu_principal, tearoff=0)
  # Agregamos una nueva opción al submenu
  submenu_ayuda.add_command(label='Acerca De')
  # Agregamos al menú principal este nuevo submenú
  menu_principal.add_cascade(menu=submenu_ayuda, label='Ayuda')
  # Mostramos el menú en la ventana principal
  ventana.config(menu=menu_principal)
   
    
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

crear_menu()

ventana.mainloop()