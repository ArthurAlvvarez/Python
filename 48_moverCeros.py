numeros = [0, 1, 0, 3, 12, 0, 5]
ceros = []

for i in numeros:
    if i == 0:
        ceros.append(i)
        numeros.remove(i)
lista = numeros + ceros
print(lista)