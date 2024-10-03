Primos = []
n = int(input("Dime un numeros y te digo todos los numeros primos menores"))

for i in range(1, n):
    cont = 0
    for j in range(1, i):
        if(i % j == 0):
            cont += 2
    if(cont == 2):
        Primos.append(i)
print(Primos)
        