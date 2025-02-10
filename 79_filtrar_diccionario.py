nombres = {
    "Arthur" : 23,
    "Alvarito" : 20,
    "Emi" : 32
}

dic ={}

for i in nombres:
    if nombres[i] > 30:
        dic[i] = nombres[i]
print(dic)
