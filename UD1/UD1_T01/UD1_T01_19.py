# Define una clase Empleado con atributos nombre, sueldo. 
# Hereda Gerente que añade departamento y Programador que añade lenguaje. 
# Implementa un método __str__ adecuado en cada clase.

class Empleado ():
    def __init__(self,sueldo, nombre):
        self.nombre = nombre
        self.sueldo = sueldo
    
    def __str__(self):
        return f"Empleado con nombre : {self.nombre} y sueldo {self.sueldo}"
    

class Gerente(Empleado):
    def __init__(self, sueldo, nombre, departamento):
        super().__init__(sueldo, nombre)
        self.departamento = departamento

    def __str__(self):
        return super().__str__()+ f"Gerente del departamento {self.departamento}"

class Programador(Empleado):
    def __init__(self, sueldo, nombre, lenguaje):
        super().__init__(sueldo, nombre)
        self.lenguaje = lenguaje

    def __str__(self):
        return super().__str__() + f"Programador en {self.lenguaje}"
    

if __name__ == "__main__":
    pepe = Empleado("Pepe", 1000)

    antonio = Gerente("Antonio",2000,"Ventas")

    paco = Programador("paco",2000,"Ventas")

    empleado = [pepe,antonio,paco]

    for e in empleado:
        print(e)