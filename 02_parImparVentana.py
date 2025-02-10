import tkinter as tk

def par_impar():
    try:
        num1 = int(entrada1.get())
        if num1 % 2 == 0:
            resultado.config(text = f'Par')
        else:
            resultado.config(text = f'impar')
    except ValueError:
        resultado.config(text = 'Error')

ventana = tk.Tk()
ventana.title("EEEEEEpa")

entrada1 = tk.Entry(ventana)
entrada1.grid(column= 0, row= 0, padx=10, pady=10 )

boton = tk.Button(ventana, text='dale', command=par_impar)
boton.grid(column= 0,row=1,pady=10)
resultado = tk.Label(ventana)
resultado.grid(column= 0,row=2,pady=10)

ventana.mainloop()