n = input("Dime cosas para añadir a la lista. Escribe Fin para terminar la lista")
lista =[]
resultado = ""
while(n != "fin"):
    n = input("Dime cosas para añadir a la lista. Escribe Fin para terminar la lista")
    lista.append(n)

postivos = []
negativos = []


for i in lista:
    if i < "0":
        negativos.append(i)
    elif i >= "0":
        postivos.append(i)

match resultado:
    case  _ if len(postivos) == len(lista):
        print("Contiene solo numeros positivos")
    case  _ if len(postivos) + len(negativos) == len(lista):
        print("Mezclado pos y neg")
    case _ if len(negativos) == len(lista):
        print("negativo")
    case _ if not lista:
        print("No hay na")
    case _:
        print("De to")