numero = 0
array = []
dic ={
    "pares" : [],
    "impares" : []
}
while numero != -1:
    array.append(numero)
    numero = int(input("Añade numeros, escribe -1 para parar: "))

for i in array:
    if i % 2 == 0:
        dic["pares"].append(i)
    else:
        dic["impares"].append(i)
print(dic) 