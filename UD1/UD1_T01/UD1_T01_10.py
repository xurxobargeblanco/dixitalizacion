# Pide al usuario dos puntos (x, y) y calcula la distancia euclidiana entre ellos.


import math

x1 = float(input("Introduce a x do punto 1: "))
y1 = float(input("Introduce a y do punto 1: "))
punto1 = (x1, y1)

x2 = float(input("Introduce a x do punto 2: "))
y2 = float(input("Introduce a y do punto 2: "))
punto2 = (x2, y2)

distancia = math.sqrt((punto2[0] - punto1[0])**2 + (punto2[1] - punto1[1])**2)
print(f"A distancia euclidiana e: {distancia}")   

