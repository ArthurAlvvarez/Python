numeros= [1,2,3,4,5,6,7,8,9,10]
n = int(input("dime un numero del 1 al 10"))
mayor = []
menor = []
for i in numeros:
    if( i< n):
        menor.append(i)
    else:
        mayor.append(i)
print(menor, " ", mayor)