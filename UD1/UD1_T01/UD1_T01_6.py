# Números primos en un rango
# Pide al usuario dos enteros a y b e imprime todos los números primos entre a y b.

def es_primo(n):
    primo = n >= 2
    d = 2
    while primo and d * d <= n:
        if n % d == 0:
            primo = False
        d += 1
    return primo


a = int(input("(A) Introduce un número mayor o igual a 1: "))
b = int(input("(B) Introduce un número mayor que 'a': "))

for n in range(a, b + 1):
    if es_primo(n):
        print(n)