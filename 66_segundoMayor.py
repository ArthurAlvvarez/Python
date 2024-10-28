lista = [11,2,80,4,90]
cont = 0
temp = 0

while cont < 2:
    for i in range(len(lista)-1):
        if lista[i] < lista[i+1]:
            temp = lista[i]
    lista.remove(temp)
    cont += 1
print(temp)