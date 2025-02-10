stock = {}

opcion = -1

while opcion != 0:
    opcion = int(input("¿Quieres hacer?:\n1. Añadir producto\n2. Modificar\n3. Eliminar producto\n0. Salir"))
    match opcion:
        case 1:
            producto = input("Dime el producto a añadir: ")
            cantidad = int(input("¿Cuanto quieres añadir?: "))
            stock[producto] = cantidad
            print("Añadido")
        case 2: 
            producto = input("Dime el producto a actualizar: ")
            cantidad = int(input("¿A que cantidad quieres actualizar?: "))
            stock[producto] = cantidad
            print("Actualizado")
        case 3:
            producto = input("Dime el producto a eliminar: ")
            stock.pop(producto)
            print("Borrado")
        case 0:
            print("Adioooooosss chaval")
        case _:
            print("Del 0 al 3 máquina")
print(stock)