import tkinter as tk

def dia():
    dia = int(entrada1.get())
    match dia:
        case 1:
            resultado.config(text = f'El día de la semana es Lunes')
        case 2:
            resultado.config(text = f'El día de la semana es Martes')
        case 3:
            resultado.config(text = f'El día de la semana es Miércoles')
        case 4:
            resultado.config(text = f'El día de la semana es Jueves')
        case 5:
            resultado.config(text = f'El día de la semana es Viernes')
        case 6:
            resultado.config(text = f'El día de la semana es Sábado')
        case 7:
            resultado.config(text = f'El día de la semana es Domingo')

ventana = tk.Tk()
ventana.title('Vamos')

entrada1 = tk.Entry(ventana)
entrada1.grid(row = 0, column=0, columnspan=2, padx=10 , pady=10)

boton = tk.Button(ventana, text= 'dale', command=dia)
boton.grid(row = 1, column=0, columnspan=2, padx=10 , pady=10)

resultado = tk.Label(ventana)
resultado.grid(row = 2, column=0, columnspan=2, pady=10)

ventana.mainloop()