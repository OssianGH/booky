from modelo.ranura_factura import RanuraFactura


class Factura:
    def __init__(self, numero, cedula, fecha, forma_pago):
        self.numero = numero
        self.cedula = cedula
        self.fecha = fecha
        self.forma_pago = forma_pago
        self.detalle: list[RanuraFactura] = []

    def agre_item(self, item):
        self.detalle.append(item)

    def elim_item(self, index):
        self.detalle.pop(index)

    def index(self, isbn):
        for i, item in enumerate(self.detalle):
            if item.isbn == isbn:
                return i
        raise ValueError(f"No se ha encontrado un libro con isbn {isbn}.")

    def total(self):
        return sum(item.cantidad * item.precio for item in self.detalle)
