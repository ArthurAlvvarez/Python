import tkinter as tk

def tabla_multiplicar():
    try:
        num1 = int(entrada1.get())
        resultado_text = ""
        for i in range(1, 11):
            resultado_text += f"{num1} x {i} = {num1 * i}\n"
        resultado.config(text=resultado_text)
    except ValueError:
        resultado.config(text="Por favor, ingrese un número válido")

ventana = tk.Tk()
ventana.title('Multiplicame')

entrada1 = tk.Entry(ventana)
entrada1.grid(row = 0, columnspan= 2, column=0, padx=10, pady=10)

boton = tk.Button(ventana, text='Dale',command=tabla_multiplicar)
boton.grid(row = 1, columnspan= 2, column=0, padx=10, pady=10)

resultado = tk.Label(ventana)
resultado.grid(row = 2, column=0, columnspan=2, pady=10)

ventana.mainloop()