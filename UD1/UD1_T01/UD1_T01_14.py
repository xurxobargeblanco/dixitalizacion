def calcularNumeros(lista):

    minimo = min(lista)
    maximo = max(lista)
    media = sum(lista) / len(lista)

    return minimo, maximo, media

numeros = [4, 7, 1, 9]

minimo, maximo, media = calcularNumeros(numeros)

print(minimo + "|" + maximo + "|" + media)
