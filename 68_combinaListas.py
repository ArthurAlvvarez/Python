lista = [1,2,3]
lista2 = [4,5,6,7]

while len(lista) < len(lista2) | len(lista) > len(lista2):
    if len(lista) < len(lista2):
        lista.append("None")
    elif len(lista) > len(lista2):
        lista2.append("None")
tupla = (lista + lista2)
print(tupla)