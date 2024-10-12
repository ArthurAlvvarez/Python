lista = [1,2,3,-5]
temp = lista[0]
lista[0] = lista[-1]
lista[-1] = temp

print(lista)