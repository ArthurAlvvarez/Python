tabla = int(input("Dime que tabla de multiplicar quieres"))
fin = int(input("Hasta que numero vas a multiplicar"))

for i in range(1, fin +1):
    resultado =  tabla * i
    print(tabla, " x " ,i, " = ", resultado)
    