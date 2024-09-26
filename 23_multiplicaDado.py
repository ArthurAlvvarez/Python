numeros = [1, 2, 3, 4, 5,6,7,8,9,10]
n = int(input("Dime un numero por el que multiplicar mi lista"))
m = []
for i in range(0,len(numeros)):
    m.append(numeros[i] * n)
print(m)