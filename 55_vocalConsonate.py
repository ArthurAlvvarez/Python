vocales = ["a","e","i","o","u"]
consonantes = ["q","w","e","r","t","y","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
letra = input("Dime una letra")

match letra:
    case _ if letra in vocales:
        print("Es una vocal")
    case _ if letra in consonantes:
        print("Es una consonante")
    case _:
        print("Simbolo raro")