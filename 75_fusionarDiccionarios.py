mate = {
    "Antonio": 5,
    "Josu":4
}

ciencias = {
    "Antonio": 7,
    "Josu":8
}

estudiantes = {}

for i in mate:
    if i in ciencias:
        estudiantes[i] = ["Mates: " + str(mate[i]) + ", Ciencias: " + str(ciencias[i])]
print(estudiantes)