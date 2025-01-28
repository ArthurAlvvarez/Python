import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Mi primera interfaz gráfica")

def saludar():
    messagebox.showinfo("EYYYY YOUUUU")

boton = tk.Button(ventana, text="KLK", command=saludar)
boton.pack(pady = 100, padx= 150)

ventana.mainloop()