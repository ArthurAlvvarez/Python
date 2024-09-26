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
numeros.sort(reverse=True)
print(numeros)