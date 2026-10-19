import random

# Juego de adivinanza
# El programa genera un número aleatorio entre 1 y 100. El usuario debe adivinarlo recibiendo pistas de "mayor" o "menor".

numero = random.randint(1, 100)
intentos = 0
adivinado = False

while not adivinado:
    respuesta = int(input("Adivina el número entre 1 y 100: "))
    intentos += 1

    if respuesta < numero:
        print("El número secreto es mayor.")
    elif respuesta > numero:
        print("El número secreto es menor.")
    else:
        print("¡Correcto! Has adivinado el número.")
        print(f"Lo has conseguido en {intentos} intentos.")
        adivinado = True

