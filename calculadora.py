import tkinter as tk
i = 0
j = 0
ventana = tk.Tk()
ventana.title("eeeeepa")


def suma():
    global i
    i = int(texto.get(1.0,tk.END)) 
    texto.delete(1.0,tk.END)

def igual():
    global i, j
    j = int(texto.get(1.0,tk.END))
    resultado = i+j
    texto.delete(1.0,tk.END)
    texto.insert(tk.END, resultado)


suma = tk.Button(ventana, text= "+", command=suma)
suma.grid(row = 1,column = 0)
resultado = tk.Button(ventana, text= "=", command=igual)
resultado.grid(row = 1,column = 1)

texto = tk.Text(ventana,width=20,height=5)
texto.grid(row=0)


tk.mainloop()