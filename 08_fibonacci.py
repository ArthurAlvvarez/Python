n = int(input("dime que posicion de fibonacci quieres saber"))

a = 0
b = 1
for i in range(n):
    print(a ,end = " ")
    a, b = b, a + b