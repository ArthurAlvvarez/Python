n1 = int(input("Dime numero par de dividendo"))
n2 = int(input("Dime numero par de divisor"))
temp = n2
cont = 1
for i in range(n2, n1):
    if(temp < n1):
        temp += n2
        cont += 1
print("El cociente de la division: ", n1, "/", n2, " es: ", cont, " y el resto es: ", n1%n2)