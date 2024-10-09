n = int(input("Dime de que numeros quieres sacar multiplos"))
max = int(input("cuantos te digo"))
multiplos = []

for i in range(1,max+1):
    multiplos.append(n*i)
print(multiplos)