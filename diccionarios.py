diccionario = {"a":1,"b":2,"c":3}
diccionario["c"] = 4
print(diccionario)
#solo el key
for i in diccionario:
        print(i)
        #solo el value
for i in diccionario:
        print(diccionario[i])
for i,j in diccionario.items():
        print(i,j)

anidado1 = {"a":1,"b":2,"c":3}
anidado2 = {"a":1,"b":2,"c":3}

d = {"a":anidado1,"b":anidado2}
print(d) 
d.clear()
#keys y values
diccionario = {"a":1,"b":2,"c":3}
it = d.items()
print(it)

diccionario = {"a":1,"b":2,"c":3}
print(list(it))
print(list(it)[0][0])#imprime a
print(list(it)[0][1])#imprime 1

diccionario = {"a":1,"b":2,"c":3}
k = d.keys()
print(k)
print(list(k))
#elimina una posi en concreto
diccionario = {"a":1,"b":2,"c":3}
d.pop("a")
print(d)

diccionario = {"a":1,"b":2,"c":3}
d.popitem()
print(d)
#elimina todas uan posi aleatoria

#actualiza sobreponiendola y añade un valor
d1 = {"a":1,"b":2,"c":3}
d2 = {"a":0,"b":2,"d":3}
d1.update(d2)
print(d1)

sorted(diccionario)
