# Solicita al usuario nombres y calificaciones de varios alumnos (hasta que escriba "fin"). Al final muestra:
# Nota media
# Nota más alta
# Nota más baja

nombre = ""
alumnos = {}
while nombre != "fin":
    nombre = input("Dime el nombre del alumno[\"fin\" para cerrar]: ")
    nota = int(input(f"Dime la nota de ${nombre}: "))
    alumnos[nombre] = nota
    