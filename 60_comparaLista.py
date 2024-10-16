n = input("Dime cosas para añadir a la lista. Escribe Fin para terminar la lista")
lista =[]
lista2 =[]
resultado = ""

while(n != "fin"):
    n = input("Dime cosas para añadir a la lista. Escribe Fin para terminar la lista")
    lista.append(n)

n = input("Dime cosas para añadir a la lista 2. Escribe Fin para terminar la lista")
while(n != "fin"):
    n = input("Dime cosas para añadir a la lista 2. Escribe Fin para terminar la lista")
    lista2.append(n)

match resultado:
    case _ if lista == lista2:
        print("Son identicas")
    case _ if lista.sort() == lista2.sort():
        print("Son identicas con orden diferente")
    case _ if len(lista) != len(lista2):
        print("Tienen diferentes tamaños")
    case _:
        print("No hay elementos en comun")