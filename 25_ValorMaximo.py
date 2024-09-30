numeros = [1,9,4,6,2,7]
temp = 0
for i in range(0, len(numeros)):
    if(temp < numeros[i]):
        temp = numeros[i]
print(temp)