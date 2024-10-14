dia = input("que dia es: ")

match dia:
    case "lunes" | "martes" | "miercoles" | "jueves" | "viernes":
        print("Dia laborable")
    case "sabado" | "domingo":
        print("Dia no laborable")
    case _:
        print("Eso no es un dia")