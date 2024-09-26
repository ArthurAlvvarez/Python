mi_lista =[2,1,"hola",False]
mi_lista2 =[3,1]

mi_lista.append(3)
print(mi_lista)

mi_lista.remove(3)
print(mi_lista)

mi_lista.pop

print(len(mi_lista))

mi_lista2.extend(mi_lista)
print(mi_lista2)

mi_lista2.insert(2,"Pepe")
print(mi_lista2)

print(mi_lista2.index("hola"))

print(mi_lista2.count(1))
#mi_lista2.sort()
#mi_lista2.reverse()
nueva_lista = mi_lista2.copy()
print(mi_lista2.clear())

numeros = [5, 2, 9, 1, 5, 6]
numeros1 = [1,2,3,4]
numeros2 = [1,2,3]
numeros.sort(reverse=True)

print(numeros)
print(5 in numeros)
print(8 not in numeros)

print(numeros1 > numeros2)

numeror = numeros2 *3
print(numeror)

for i in numeros2:
    print(i)

print()

for index, i in enumerate(numeros2):
    print(index ,i)

print()

cadena = "hola"
for index, i in enumerate(cadena):
    print(index, i)

print()

lista1 = [1,2,3]
lista2 = ["h","z","r"]
for lista1, lista2 in zip(lista1,lista2):
    print(lista1,lista2)

print()

print(mi_lista[0]+5)
print(mi_lista[2].upper())
print(mi_lista[3] or True)
if "hola" in mi_lista:
    print("La palabra está")
else:
    print("no está")

print()
