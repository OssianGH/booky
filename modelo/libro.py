from modelo.transaccion import Transaccion


class Libro:
    def __init__(self, isbn, titulo, precio_compra, precio_venta, stock, ruta_imagen):
        self.isbn = isbn
        self.titulo = titulo
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.stock = stock
        self.ruta_imagen = ruta_imagen
        self.transacciones: list[Transaccion] = []

    def agre_transaccion(self, transaccion):
        self.transacciones.append(transaccion)

    def l_transacciones(self, query=""):
        return [t for t in self.transacciones if t.tipo.startswith(query)]

    class Criterio:
        isbn = "ISBN"
        titulo = "Título"
