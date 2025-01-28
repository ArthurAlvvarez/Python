alumnos = {
    "Alvaro": [4, 5],
    "Emi": [6, 8]
}

promedios = {}

for estudiante, calificaciones in alumnos.items():
    promedio = sum(calificaciones) / len(calificaciones)
    promedios[estudiante] = promedio

print(promedios)