from functools import reduce

numeros = [2, 3, 4]

resultado = reduce(lambda a, b: a * b, numeros)

print("O produto é:", resultado)