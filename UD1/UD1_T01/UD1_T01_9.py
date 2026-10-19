# Diccionario de frecuencias de palabras
# Pide al usuario una frase y construye un diccionario con la frecuencia de cada palabra.

frase = input("Introduce una frase: ")

palabras = frase.lower().split()

frecuencias = {}

for palabra in palabras:
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1

print(frecuencias)
