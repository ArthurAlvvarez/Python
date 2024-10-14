lados = int(input("Cuantos lados tiene tu figura: "))

match lados:
    case 1: 
        print("circulo")
    case 2:
        print("Es un digono")
    case 3:
        print("Es un triangulo")
    case _:
        print("No tengo esa figura")