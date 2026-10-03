# Gestión de notas
# Solicita al usuario nombres y calificaciones de varios alumnos (hasta que escriba "fin"). Al final muestra:
#
#   - Nota media
#   - Nota más alta
#   - Nota más baja

nombre = input("Nombre del alumno (o 'fin' para terminar): ")

suma = 0
cantidad = 0
nota_max = 0
nota_min = 10

while nombre != "fin":
    nota = float(input(f"Nota de {nombre}: "))
    suma += nota
    cantidad += 1
    if nota > nota_max:
        nota_max = nota
    if nota < nota_min:
        nota_min = nota
    nombre = input("Nombre del alumno (o 'fin' para terminar): ")

if cantidad > 0:
    print("Nota media:", round(suma / cantidad, 2))
    print("Nota más alta:", nota_max)
    print("Nota más baja:", nota_min)
else:
    print("No se introdujo ningún alumno")

