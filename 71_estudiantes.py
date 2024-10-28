estudiantes = {
    "Emi":"A",
    "Pacheco":"A",
    "Alvarito":"P"
}

alumno = input("Dime un alumno: ")
print(estudiantes.get(alumno,"No tengo ese alumno"))