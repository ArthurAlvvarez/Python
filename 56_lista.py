lista = [1,2]
match lista:
    case _ if not lista:
        print("Vacia")
    case _ if len(lista) == 1:
        print("Un solo elemento")
    case _ if len(lista) > 1:
        print(len(lista), " elementos")