numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
n = 0
if(len(numeros) % 2 == 0):
    n = int((len(numeros)+1) /2)
    print((numeros[n] + numeros[n-1])/2)
else:
    n = int(len(numeros)/2)
    print(numeros[n])