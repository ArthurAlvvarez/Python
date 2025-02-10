import tkinter as tk

def mayor_menor():
    try:
        num1 = int(entrada1.get())
        num2 = int(entrada2.get())
        if num1 < num2:
            resultado.config(text = f'{num1} es menor y {num2} es mayor')
        else:
            resultado.config(text = f'{num2} es menor y {num1} es mayor')
    except ValueError:
        resultado.config(text='error')

ventana = tk.Tk()
ventana.title('HOOOOLAAA')

entrada1 = tk.Entry(ventana)
entrada2 = tk.Entry(ventana)

entrada1.grid(column= 0, row= 0, padx=10, pady=10 )
entrada2.grid(column= 1, row= 0, padx=10, pady=10 )

boton = tk.Button(ventana, text='dale', command=mayor_menor)
boton.grid(column= 0,columnspan=2, row= 1, pady=10 )

resultado = tk.Label(ventana)
resultado.grid(column= 0,columnspan=2, row= 2, pady=10 )

ventana.mainloop()