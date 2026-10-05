# Implementa una clase Cuenta con saldo inicial y métodos para ingresar, retirar y mostrar saldo. Añade control de fondos insuficientes.

class Cuenta:

    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def ingresar(self, dinero_ingresado):
        self.saldo += dinero_ingresado

    def retirar(self, dinero_retirar):
        if self.saldo < dinero_retirar:
            print("Saldo insuficiente")
        else:
            self.saldo -= dinero_retirar

    def mostrar_saldo(self):
        print(f"O teu saldo: {self.saldo}")


if __name__ == "__main__":
    saldo = int(input("Introduce el saldo inicial: "))

    cuenta_0 = Cuenta(saldo)
    cuenta_0.mostrar_saldo()
    cuenta_0.ingresar(200)
    cuenta_0.retirar(10)
    cuenta_0.mostrar_saldo()