lista = [1,2,3,-5]
negativo = True
for i in lista:
    if i < 0 :
        negativo = False
if negativo == False:
    print("Hay numeros negativos en la lista")
else:
    print("Lista positiva")