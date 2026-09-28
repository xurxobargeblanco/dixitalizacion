# Ordenación de palabras
# El usuario introduce una frase. Muestra las palabras ordenadas alfabéticamente y por longitud.

frase = input("Introduce una frase para ordenar sus palabras")

palabras = sorted(frase.split(), key=str.lower)

ordenadas = sorted(palabras,key=len)

print(ordenadas)