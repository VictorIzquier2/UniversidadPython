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

entrada1.config(state='readonly')

ventana.mainloop()