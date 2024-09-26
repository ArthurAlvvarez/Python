letras = ["a","e","i","o","u"]

palabra = "Hola"
cont = 0
for i in palabra.lower():
    if i in letras:
        cont += 1
print(cont)

