# Frecuencia de caracteres
# Pide al usuario una cadena y cuenta cuántas veces aparece cada carácter usando un diccionario.

texto = input("Introduce unha cadea de textro:")
frecuencia = {}

for c in texto:
    if c != ' ' :
        frecuencia[c] = frecuencia.get(c,0) +1

print(frecuencia)

