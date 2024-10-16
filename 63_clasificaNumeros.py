lista = [1, "hola", 3.14, True, 42, "mundo", False]
resultado = ""
enteros = []
texto = []
boolean = []
datos = []

for i in lista:
    match i:
        case _ if isinstance(i, bool):
            boolean.append(i)
        case _ if isinstance(i, int):
            enteros.append(i)
        case _ if isinstance(i, str):
            texto.append(i)
        case _:
            datos.append(i)
lista = [enteros,boolean,texto,datos]
print(lista)