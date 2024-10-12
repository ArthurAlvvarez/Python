palabras = ["sol", "luna", "mar", "estrella", "cielo"]
l = input("Dime una letra")

for i in palabras:
    if i.startswith(l):
        print(i)