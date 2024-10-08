numeros = [5, 3, 5, 3, 2, 3, 8, 5, 1, 9, 3, 4]
temp = 0
n = 0
n2 = 0
for i in range(len(numeros)):
    cont = 1
    n = numeros [i]
    for j in range(i,len(numeros)-1):
        if(numeros[i] == numeros[j +1]):
            cont += 1
    if(cont > temp):
        temp = cont
        n2 = n
print("El numero ",n2 ," se repite ", temp, " veces")