agenda = {}

nome = input("Introduce o nome do contacto: ")
telefono = int(input("Introduce o teléfono: "))

if nome in agenda:
    agenda[nome].append(telefono)
else:
    agenda[nome] = [telefono]

buscar = input("Que contacto queres buscar? ")

if buscar in agenda:
    print("Contacto:", buscar)
    print("Teléfonos:", agenda[buscar])
else:
    print("O contacto non existe.")

print(agenda)

