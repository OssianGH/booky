class Transaccion:
    def __init__(self, tipo, cantidad, fecha):
        self.tipo = tipo
        self.cantidad = cantidad
        self.fecha = fecha

    class Tipo:
        abastecimiento = "Abastecimiento"
        venta = "Venta"
