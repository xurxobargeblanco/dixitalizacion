
def contador(nome_ficheiro):

    with open(nome_ficheiro, "r") as file:
        texto = file.read()

    liñas = texto.splitlines()
    palabras = texto.split()
    caracteres = len(texto)

    return len(liñas), len(palabras), caracteres


resultado = contador("texto.txt")

print("Liñas:", resultado[0])
print("Palabras:", resultado[1])
print("Caracteres:", resultado[2])