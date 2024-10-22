d ={
    "Lg":45,
    "Asus":60,
    "Roge":90
}
producto = input("Dime un producto: ")

if producto in d:
    print(d[producto])
else:
    print("No lo tenemos")