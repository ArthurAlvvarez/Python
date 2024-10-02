lista = [3, 7, 2, 5, 3, 9, 1, 4, 2, 6, 8, 5, 7, 2, 3, 10, 9, 1, 4, 6]
lista.sort()
lista2 =[]
n1 = int(input("Dime un numero del 1 al 10"))
for i in range(len(lista)):
    if(n1 <= lista[i]):
        lista2.append(lista[i])
print(lista2)