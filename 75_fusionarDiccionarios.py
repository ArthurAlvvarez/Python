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
        estudiantes[i] = {"Mate" : mate[i],
        "ciencias": ciencias[i]}
print(estudiantes)