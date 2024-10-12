lista = [1,2,3,4,5,6]
pares = 0
impares = 0
for i in lista:
    if(i % 2 == 0):
        pares += 1
    else:
        impares += 1
print("Hay ",pares," pares y ", impares, " impares")