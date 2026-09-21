# Números pares e impares

numeros = map(int, input("Introduce una serie de numeros pares e impares separados por espacios").split())

lista_numeros_pares = [n for n in numeros if n%2 == 0]
lista_numeros_inpares = [n for n in numeros if n%2 != 0]

print(f"Pares : {lista_numeros_pares}")
print(f"Inpares : {lista_numeros_inpares}")