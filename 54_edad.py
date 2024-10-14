edad = int(input("Dime tu edad frate: "))

match edad:
    case _ if ( 0 <= edad <= 12):
        print("Niño")
    case _ if (13 <= edad <= 17):
        print("adolescente")
    case _ if (18 <= edad <= 67):
        print("adulto")
    case _ if (65 <= edad):
        print("viejo")
    case _:
        print ("Esa edad no es una edad")