lista = [1]
lista2 = [lista,1]

for i in lista2:
    match i:
        case _ if isinstance(i,list):
            lista2.remove(i)
        case _ if not lista2:
            print("No hay lista")

match lista2:
    case _ if not lista2:
        print("No hay lista")
    case _:
        print(lista2)