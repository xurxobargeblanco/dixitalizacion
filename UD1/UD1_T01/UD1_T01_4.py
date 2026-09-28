# Calculadora básica
# Implementa una calculadora que acepte dos números y una operación (+, -, *, /) introducidos por consola.

A = float(input("Introduce el primer operando"))
B = float(input("Introduce el segundo operando"))

operacion = input("Que operacion deseas realizar ? (+, -, *, /) ")

match operacion:
    case '+' : 
        resultado = A+B
        print(f"Resultado : {resultado}")
    case '-' : 
        resultado = A-B
        print(f"Resultado : {resultado}")
    case '*' : 
        resultado = A*B
        print(f"Resultado : {resultado}")
    case '/' :
        if B == 0 : print("No se puede realizar división entre 0")
        else : 
            resultado = A/B
            print(f"Resultado : {resultado}")
    case _: 
        print("Operación no válida")

