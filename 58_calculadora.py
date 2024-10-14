simbolo = input("Quieres sumar, restar, dividir o multiplicar. (+, -, *, /) : ")
n = int(input("Dime el primer numero: "))
n2 = int(input("Dime el segundo numero: "))

match simbolo:
    case "+":
        print(n, " + ", n2, " = ", n + n2)
    case "-":
        print(n, " - ", n2, " = ", n - n2)
    case "*":
        print(n, " * ", n2, " = ", n * n2)
    case "/":
        print(n, " / ", n2, " = ", n / n2)
    case _:
        print("No se que simbolo es ese")