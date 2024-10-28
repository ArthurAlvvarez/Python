lista = [11,11,11,2,2,80,4,90]
n = int(input("Dime el numero de veces que se tiene que repetir un numero para eliminarlo de la lista"))
lista2 = []

for i in range(len(lista)-1):
    if lista.count(lista[i]) < n:
        lista2.append(lista[i])
print(lista2)