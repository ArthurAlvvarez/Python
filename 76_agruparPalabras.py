palabras = ["hola", "klk", "epa"]
dic = {}

for i in palabras:
    longitud = len(i)
    if longitud not in dic:
        dic[longitud] = [i] 
    else:
        dic[longitud].append(i)  
print(dic)

