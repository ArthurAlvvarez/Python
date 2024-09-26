conversion = str(input("¿convertir de F a C o de C a F, escribe F o C?"))
if(conversion == "F"):
    farenheit = float(input("Dime los farenheit"))
    print("Celsius: ", (farenheit - 32) * 5/9)
else:
    celsius = float(input("Dime los celsius"))
    print("Celsius: ", (celsius * 9/5) + 32)