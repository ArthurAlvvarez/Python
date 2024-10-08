numeros = [42, 7, 19, 56, 3, 88, 23, 5, 91, 14]
temp = 0
for i in range(len(numeros)-1):
    for j in range(i,len(numeros)-1):
        if(numeros[i]> numeros [j +1]):
            temp = numeros[i]
            numeros[i] = numeros[j +1]
            numeros[j +1] = temp
print(numeros)