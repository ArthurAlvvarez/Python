numeros = [5, 3, 5, 3, 2, 3, 8, 5, 1, 9, 3, 4]
n = int(input("Dime un numero de la lista"))
n2 = int(input("Dime por que numero lo cambio"))
for i in range(len(numeros)):
    if(n == numeros[i]):
        numeros[i] = n2
print(numeros)