mi_lista = []
while True:
    entrada = input("Dime cosas para la lista, escribe fin para acabar")
    if(entrada != "fin"):
        mi_lista.append(entrada)
    else:
        print(mi_lista[0], mi_lista[-1])
        False
