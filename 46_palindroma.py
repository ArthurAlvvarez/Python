lista = [1,"oso,",1]
w = -1

for i in lista:
    if(i == lista[w]):
        w += -1
    if(w == len(lista)*-1):
        print("Es palindroma")
