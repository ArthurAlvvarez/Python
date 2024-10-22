lista = ["a","b","c"]
d = {}

for i in range(len(lista)):
    d.update({i:lista[i]})
print(d)