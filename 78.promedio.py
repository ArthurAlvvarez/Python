alumnos = {
    "Alvaro": [4, 5],
    "Emi": [6, 8]
}

for i,j in alumnos.items():
    alumnos[i] = sum(j) / len(j)
print(alumnos)