min = int(input("desde que numero quieres que genere"))
max = int(input("hasta que numero"))
n = int(input("cuantos numeros te genero"))
numeros =[]

for i in range(min, max+1):
    numeros.append(i)

for i in range(n):
    print(numeros[i])