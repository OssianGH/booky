import pickle
from modelo.libro import Libro
from modelo.transaccion import Transaccion
from random import randint


class GestorLibro:
    libros: list[Libro] = []
    caja = 1000000.0

    @staticmethod
    def generar_isbn():
        while True:
            isbn = "978" + "".join([str(randint(0, 9)) for _ in range(10)])
            try:
                GestorLibro.index(isbn)
            except ValueError:
                return isbn

    @staticmethod
    def agregar(libro):
        GestorLibro.libros.append(libro)

    @staticmethod
    def eliminar(index):
        GestorLibro.libros.pop(index)

    @staticmethod
    def index(isbn):
        for i, libro in enumerate(GestorLibro.libros):
            if libro.isbn == isbn:
                return i
        raise ValueError(f"No se ha encontrado un libro con isbn {isbn}.")

    @staticmethod
    def abastecer(index, cantidad, fecha):
        libro = GestorLibro.libros[index]
        libro.agre_transaccion(
            Transaccion(Transaccion.Tipo.abastecimiento, cantidad, fecha)
        )
        libro.stock += cantidad

    @staticmethod
    def vender(index, cantidad, fecha):
        libro = GestorLibro.libros[index]
        libro.agre_transaccion(Transaccion(Transaccion.Tipo.venta, cantidad, fecha))
        libro.stock -= cantidad

    @staticmethod
    def libros_vendibles(query=""):
        return [
            libro
            for libro in GestorLibro.libros
            if libro.stock > 0 and str(libro.isbn).startswith(query)
        ]

    @staticmethod
    def libros_isbn(query=""):
        return [
            libro for libro in GestorLibro.libros if str(libro.isbn).startswith(query)
        ]

    @staticmethod
    def libros_titulo(query=""):
        return [
            libro
            for libro in GestorLibro.libros
            if query.lower() in libro.titulo.lower()
        ]

    @staticmethod
    def mas_costoso():
        return max(GestorLibro.libros, key=lambda l: l.precio_venta)

    @staticmethod
    def menos_costoso():
        return min(GestorLibro.libros, key=lambda l: l.precio_venta)

    @staticmethod
    def mas_vendido():
        return max(
            GestorLibro.libros,
            key=lambda l: len(l.l_transacciones(Transaccion.Tipo.venta)),
        )

    @staticmethod
    def grabar_datos():
        with open("./modelo/libros.dat", "wb") as out_file1:
            pickle.dump(GestorLibro.libros, out_file1)
            out_file1.flush()
            out_file1.close()
        with open("./modelo/caja.dat", "wb") as out_file2:
            pickle.dump(GestorLibro.caja, out_file2)
            out_file2.flush()
            out_file2.close()

    @staticmethod
    def cargar_datos():
        with open("./modelo/libros.dat", "rb") as in_file1:
            GestorLibro.libros = pickle.load(in_file1)
            in_file1.close()
        with open("./modelo/caja.dat", "rb") as in_file2:
            GestorLibro.caja = pickle.load(in_file2)
            in_file2.close()
