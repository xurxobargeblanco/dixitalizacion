# Números pares e impares

lista = str(input("Introduce una serie de numeros pares e impares separados por espacios"))
numeros = lista.split(" ")
lista_numeros_pares = []
lista_numeros_inpares = []

for c in numeros:
    if c % 2 == 0 :
       lista_numeros_pares.append(int(c)) 
    else :
        lista_numeros_inpares.append(int(c)) 

    