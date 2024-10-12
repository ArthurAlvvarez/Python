lista = [1,"oso",2]
lista2 = [2,1,"oso"]
cont = 0

for i in lista:
    if(i in lista2):
        cont += 1
if cont == len(lista):
    print("Ambas listas son iguales")
else:
    print("No son iguales las listas")