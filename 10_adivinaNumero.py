import random

n = random.randint(1,10)
intentos = 0

print("Adivina el numero del 1 al 10")

while True:
    numero = int(input("Dime un numero"))
    intentos += 1

    if numero == n:
        print("Bien hecho. Numero de intentos: ", intentos)
        break
    elif numero < n:
        print("Subele")
    elif numero > n:
        print("Bajale")