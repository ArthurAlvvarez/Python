palabras = ["hola", "klk", "epa"]
dic = {}

for i in palabras:
    longitud = len(i)
    if longitud in dic:
        dic[longitud].append(i)
    else:
        dic[longitud] = [i]
        
print(dic)
