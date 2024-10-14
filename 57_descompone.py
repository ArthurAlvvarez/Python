n = input("Dime un numero de maximo 3 numeros")

match len(n):
    case 1:
        print("Tiene ", n, " unidades")
    case 2:
        print("Tiene ", n[0], " decenas" , n[1], " unidades")
    case 3:
        print("Tiene ",n[0], " centenas", n[1], " decenas" , n[2], " unidades")
    case _:
        print("Nose")