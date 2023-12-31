import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Componentes')
ventana.iconbitmap('icono.ico')

def crear_componentes_tabulador(tabulador):
  # Agregar una etiqueta y un componente de entrada
  etiqueta1 = ttk.Label(tabulador, text='Nombre:')
  etiqueta1.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
  entrada1 = ttk.Entry(tabulador, width=30)
  entrada1.grid(row=0, column=1, padx=5, pady=5)
  
  def enviar():
    messagebox.showinfo('Mensaje', f'Nombre: {entrada1.get()}')
  # Agregamos un botón
  boton1 = ttk.Button(tabulador, text='Enviar', command=enviar)
  boton1.grid(row=1, column=0, columnspan=2)
  
def crear_componentes_tabulador2(tabulador):
  contenido = 'Este es mi texto con el contenido'
  
  # Creamos el componente de scroll
  scroll = scrolledtext.ScrolledText(tabulador, width=50, height=10, wrap=tk.WORD)
  scroll.insert(tk.INSERT, contenido)
  
  # Mostramos el componente
  scroll.grid(row=0, column=0)
  

def crear_tabs():
  # Creamos un tab control, para ello usamos la clase Notebook
  control_tabulador = ttk.Notebook(ventana)
  
  # Agregamos un marco (frame) para agregar dentro del tab y organizar
  tabulador1 = ttk.Frame(control_tabulador)
  
  # Agregamos el tabulador al control de tabuladores
  control_tabulador.add(tabulador1, text='Tabulador 1')
  
  # Mostramos el tabulador
  control_tabulador.pack(fill='both')
  
  # Creamos los componentes del tabulador 1
  crear_componentes_tabulador(tabulador1)
  
  # Creamos un segundo tabulador
  tabulador2 = ttk.LabelFrame(control_tabulador, text ='Contenido')
  control_tabulador.add(tabulador2, text='Tabulador 2')
  
  # Creamos los componentes del segundo tabulador
  crear_componentes_tabulador2(tabulador2)
  
  
  
crear_tabs()

ventana.mainloop()