import os

#se define la clase libro
class Libro:
    def __init__(self, titulo:str, autor:str, isbn:str, disponible:bool):
        """
        (Libro, str, str, bool) -> None
        Inicializa un libro con su título, autor, idbn y disponibilidad.
        """
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def cambiar_disponibilidad(self):
        """
        (Libro) -> None
        Cambia la disponibilidad del libro.        
        >>>true ->false
        >>>false ->true
        """
        self.disponible = not self.disponible

    def get_disponibilidad(self):
        """
        (Libro) -> bool
        Devuelve la disponibilidad del libro.
        >>>true
        >>>false
        """
        return self.disponible

    def get_isbn(self):
        """
        (Libro) -> str
        Devuelve el isbn del libro.
        """
        return self.isbn

    def get_info(self):
        """
        (Libro) -> str
        Devuelve la información del libro.
        """
        return f"El libro {self.titulo} de {self.autor} con isbn {self.isbn}  {'está disponible' \
                if self.disponible else 'no está disponible'}."

    def mostrar_info(self):
        """
        (Libro) -> str
        Devuelve la información del libro.
        """
        print(f"El libro {self.titulo} de {self.autor} con isbn {self.isbn} " \
                f"{'está disponible' if self.disponible else 'no está disponible'}.")

#definimos la clase biblioteca que tiene una lista de libros
class Biblioteca:
    def __init__(self):
        """
        (biblioteca) -> None
        Inicializa una biblioteca con una lista vacia de libros.
        """
        self.libros = []

    def agregar_clase_libro(self, nuevo_libro:Libro):
        """
        (biblioteca, libro) -> None
        Agrega un libro a la biblioteca.
        """
        self.libros.append(nuevo_libro)

    @staticmethod
    def validar_entrada(value):
        if value:
           return False
        else:
            print("El valor ingresado no es valido")
            return True

    def agregar_libro(self):
        """
        (biblioteca) -> None
        Agrega un libro a la biblioteca.
        """
        repetir = True
        while repetir:
            titulo = input("Ingrese el título del libro: ")
            repetir= Biblioteca.validar_entrada(titulo)
        repetir = True
        while repetir:
            autor = input("Ingrese el autor del libro: ")
            repetir= Biblioteca.validar_entrada(autor)
        repetir = True
        while repetir:
            isbn = input("Ingrese el isbn del libro: ")
            repetir= Biblioteca.validar_entrada(isbn)
        disponible = input("El libro está disponible? (s/n): ")
        disponible = True if disponible == "s" else False
        try:
            self.libros.append(Libro(titulo,autor, isbn, disponible))
        except:
            print("Error al agregar el libro")

    def prestar_libro(self, isbn:str):
        """
        (biblioteca, str) -> None
        Presta un libro de la biblioteca.
        """
        try:
            libros = self.buscar_libro(isbn)
        except:
            print("Error al buscar el libro")
        if len(libros) > 0:
            for libro in libros:
                if libro.get_disponibilidad():
                    libro.cambiar_disponibilidad()
                    print("Libro prestado.")
                    return
            print("El libro no está disponible.")
        else:
            print("El libro no está en la biblioteca.")

    def devolver_libro(self, isbn:str):
        """
        (biblioteca, str) -> None
        Devuelve un libro a la biblioteca.
        """
        libros = self.buscar_libro(isbn)
        if len(libros) > 0:
            for libro in libros:
                if not libro.get_disponibilidad():
                    libro.cambiar_disponibilidad()
                    print("Libro devuelto.")
                    return
            print("El libro no está prestado.")
        else:
            print("El libro no está en la biblioteca.")

    def mostrar_libros(self):
        """
        (biblioteca) -> str
        Muestra los libros de la biblioteca.
        """
        #print('\n'.join([libro.get_info() for libro in self.libros]))
        if len(self.libros) > 0:
            max_titulo = max(len(libro.titulo) for libro in self.libros)
            max_autor = max(len(libro.autor) for libro in self.libros)
            max_isbn = max(len(libro.isbn) for libro in self.libros)
            print("*" * (max_titulo + max_autor + max_isbn + 20))
            print(f"* {'Título':<{max_titulo}} * {'Autor':<{max_autor}} * {'ISBN':<{max_isbn}} * " \
                    f"{'Disponibilidad':<14} *")
            print("*" * (max_titulo + max_autor + max_isbn + 20))
            for libro in self.libros:
                print(f"* {libro.titulo:<{max_titulo}} * {libro.autor:<{max_autor}} * " \
                        f"{libro.isbn:<{max_isbn}} * " \
                        f"{'Disponible' if libro.disponible else 'No disponible':<14} *")
            print("*" * (max_titulo + max_autor + max_isbn + 20))
        else:
            print("No hay libros en la biblioteca.")

    def buscar_libro(self, isbn:str):
        """
        (biblioteca, str) -> list
        Busca un libro por su isbn.
        """
        return  list(filter(lambda libro: libro.isbn == isbn , self.libros))



class Sistema:
    def __init__(self):
        """
        (Menu) -> None
        Inicializa un menú con opciones para la biblioteca.
        """
        self.opciones = {
            "1": "Agregar libro",
            "2": "Prestar libro",
            "3": "Devolver libro",
            "4": "Mostrar libros",
            "5": "Buscar",
            "6": "Salir"
        }
    def mostrar_menu(self):
        """
        (Menu) -> None
        Muestra las opciones del menú.
        """
        print("Menú:")
        print('*'*21)
        for key, value in self.opciones.items():
            cadena = f"* {key}: {value}"
            longitud_cadena = len(cadena)
            if longitud_cadena < 20:
                espacios_necesarios = 20 - longitud_cadena
                cadena = cadena + " " * espacios_necesarios + '*'
            print(cadena)
            print('*                   *')
        print('*'*21)

    def limpiar_pantalla(self):
        """
        (Menu) -> None
        Limpia la pantalla.
        """
        os.system('cls' if os.name == 'nt' else 'clear')


    def seleccionar_opcion(self):
        """
        (Menu) -> str
        Selecciona una opción del menú.
        """
        print()
        opcion = input("Seleccione una opción: ")
        while opcion not in self.opciones.keys():
            print("Opción inválida.")
            print()
            opcion = input("Seleccione una opción: ")
        return opcion

    def agregar_libro(self, biblioteca:Biblioteca):
        """
        (Biblioteca) -> None
        Agrega un libro a la biblioteca.
        """
        error= False
        while not error:
            try:
                biblioteca.agregar_libro()
                print("Libro agregado correctamente.")
                error = True
            except:
                print("Error al agregar el libro")
        self.pausar()

    def prestar_libro(self, biblioteca:Biblioteca):
        """
        (Menu) -> None
        Presta un libro de la biblioteca.
        """
        isbn = input("Ingrese el isbn del libro: ")
        biblioteca.prestar_libro(isbn)
        self.pausar()

    def devolver_libro(self, biblioteca:Biblioteca):
        """
        (Menu) -> None
        Devuelve un libro a la biblioteca.
        """
        isbn = input("Ingrese el isbn del libro: ")
        biblioteca.devolver_libro(isbn)
        self.pausar()

    def pausar(self):
        """
        (Menu) -> None
        Pausa la pantalla.
        """
        input("Presione enter para continuar.")

    def buscar(self, biblioteca:Biblioteca):
        """
        (Menu) -> None
        Busca un libro en la biblioteca.
        """
        isbn = input("Ingrese el isbn del libro: ")
        libros = biblioteca.buscar_libro(isbn)
        if len(libros) > 0:
            for libro in libros:
                libro.mostrar_info()
        else:
            print("El libro no está en la biblioteca.")
        self.pausar()

libros_inicio = [
    ["Cien años de soledad", "Gabriel García Márquez", "978-0307474727", True],
    ["1984", "George Orwell", "978-0451524935", True],
    ["Orgullo y prejuicio", "Jane Austen", "978-0141439518", True],
    ["El señor de los anillos", "J.R.R. Tolkien", "978-0618260231", True],
    ["Matar un ruiseñor", "Harper Lee", "978-0061120084", True],
    ["Don Quijote de la Mancha", "Miguel de Cervantes", "978-8420471899", True],
    ["El guardián entre el centeno", "J.D. Salinger", "978-0316769174", True],
    ["Crimen y castigo", "Fyodor Dostoevsky", "978-0679734505", True],
    ["En busca del tiempo perdido", "Marcel Proust", "978-0141180331", True],
    ["Ulises", "James Joyce", "978-0679722762", True]

]

mi_biblioteca = Biblioteca()

for libro_actual in libros_inicio:
    mi_biblioteca.agregar_clase_libro(Libro(libro_actual[0], libro_actual[1], \
                                            libro_actual[2], libro_actual[3]))
sistema = Sistema()

sistema.mostrar_menu()
seleccion = int (sistema.seleccionar_opcion())
print()
while seleccion != 6:
    if seleccion == 1:
        sistema.agregar_libro(mi_biblioteca)
    elif seleccion == 2:
        sistema.prestar_libro(mi_biblioteca)
    elif seleccion == 3:
        sistema.devolver_libro(mi_biblioteca)
    elif seleccion == 4:
        mi_biblioteca.mostrar_libros()
        sistema.pausar()
    elif seleccion == 5:
        sistema.buscar(mi_biblioteca)
    print()
    sistema.mostrar_menu()
    print()
    seleccion = int (sistema.seleccionar_opcion())
    print()
