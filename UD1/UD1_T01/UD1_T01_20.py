# Diseña una clase Libro y una clase Biblioteca que almacene varios libros en una lista. 
# Implementa métodos para añadir, buscar y listar libros.

class Libro:

    def __init__(self, nombre, autor, fecha_publicacion):
        self.nombre = nombre
        self.autor = autor
        self.fecha_publicacion = fecha_publicacion

    def __str__(self):
        return f"Libro {self.nombre} con autor {self.autor} y fecha de publicación: {self.fecha_publicacion}"


class Biblioteca:

    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def anadir_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro(self, nombre):
        encontrado = None
        i = 0
        while encontrado is None and i < len(self.libros):
            if self.libros[i].nombre == nombre:
                encontrado = self.libros[i]
            i += 1
        return encontrado

    def listar_libros(self):
        for libro in self.libros:
            print(libro)


if __name__ == "__main__":
    biblioteca = Biblioteca("Municipal")

    biblioteca.anadir_libro(Libro("El Quijote", "Cervantes", 1605))
    biblioteca.anadir_libro(Libro("Rayuela", "Cortázar", 1963))

    biblioteca.listar_libros()

    resultado = biblioteca.buscar_libro("Rayuela")
    if resultado is not None:
        print("Encontrado:", resultado)
    else:
        print("No encontrado")
        
        