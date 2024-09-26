numeros = [1, 2, 3, 4, 5,6,7,8,9,10]
cont = 0
for i in range(0, len(numeros)):
    if numeros[i] % 2 == 0:
        cont = cont + 1
print(cont)