alumnos1 = {
    "Arthur" : 6,
    "Alvarito" : 6,
    "Emi" : 7
}

alumnos2 = {
    "Arthur" : 8,
    "Alvarito" : 9,
    "Emi" : 7
}

alumnos3 = {}

for i in alumnos1:
    if i in alumnos2:
        if alumnos1[i] < alumnos2[i]:
            alumnos3[i] = alumnos2[i]
print(alumnos3)