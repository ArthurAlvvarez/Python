t = int(input("Que temperatura hace: "))

match t:
    case _ if ( 0 > t ):
        print("Muy frío")
    case _ if ( 0 <= t <= 10):
        print("Frío")
    case _ if (11 <= t <= 20):
        print("Templado")
    case _ if (21 <= t <= 30):
        print("Calor")
    case _ if (30 <= t):
        print("Muy caliente")
    case _:
        print ("Esa no es una temperatura")