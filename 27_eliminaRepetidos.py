lista = [1,1,2,2,2,3,4,4,5,5]
temp = lista[0]
lista2 = []
for i in range(0,len(lista)-1):
    if(lista[i] != lista[i+1]):
        lista2.append(lista[i])
lista2.append(lista[-1])
print(lista2)