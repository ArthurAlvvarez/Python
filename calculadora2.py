import tkinter as tk


n1 = 0
n2 = 0
operator = ""

def getNumber(n):
    entrada.insert(tk.END,n)

def getOperator(o):
    global operator,n1
    operator = o
    n1 = int(entrada.get())
    entrada.delete(0,tk.END)

def getResultado():
    global operator,n1,n2
    n2 = int(entrada.get())
    entrada.delete(0,tk.END)
    match operator:
        case "+":
            resultado = n1 + n2
            entrada.insert(tk.END,resultado)
        case "-":
            resultado = n1 - n2
            entrada.insert(tk.END,resultado)


ventana = tk.Tk()
ventana.title("Calculadora")


entrada = tk.Entry(ventana, width=20)
entrada.grid(column=0, row=0, columnspan=3)



boton1 = tk.Button(ventana,text="1", command=lambda: getNumber(1))
boton2 = tk.Button(ventana,text="2", command=lambda: getNumber(2))
boton3 = tk.Button(ventana,text="3", command=lambda: getNumber(3))
boton4 = tk.Button(ventana,text="4", command=lambda: getNumber(4))
boton5 = tk.Button(ventana,text="5", command=lambda: getNumber(5))
boton6 = tk.Button(ventana,text="6", command=lambda: getNumber(6))
boton7 = tk.Button(ventana,text="7", command=lambda: getNumber(7))
boton8 = tk.Button(ventana,text="8", command=lambda: getNumber(8))
boton9 = tk.Button(ventana,text="9", command=lambda: getNumber(9))
boton0 = tk.Button(ventana,text="0", command=lambda: getNumber(0))
botonsuma = tk.Button(ventana,text="+", command=lambda: getOperator("+"))
botonresta = tk.Button(ventana,text="-", command=lambda: getOperator("-"))
botonigual = tk.Button(ventana,text="=", command= getResultado)

boton1.grid(column=0, row=1)
boton2.grid(column=1, row=1)
boton3.grid(column=2, row=1)
boton4.grid(column=0, row=2)
boton5.grid(column=1, row=2)
boton6.grid(column=2, row=2)
boton7.grid(column=0, row=3)
boton8.grid(column=1, row=3)
boton9.grid(column=2, row=3)
boton0.grid(column=1, row=4)
botonsuma.grid(column=0,row=4)
botonresta.grid(column=2,row=4)
botonigual.grid(column=1,row=5)

ventana.mainloop()