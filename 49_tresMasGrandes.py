numeros = [10, 30, 15, 2, 45, 60, 5, 100, 35]
lista = []
temp = 0
while len(lista) < 3:
    for i in range(3):
        for j in range(len(numeros)-1):
            if numeros[j] < numeros[j+1] and numeros[j+1] not in lista:
                temp = numeros[j+1]
        lista.append(temp)
print(lista)