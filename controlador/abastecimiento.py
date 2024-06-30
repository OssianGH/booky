from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox, QInputDialog
from controlador.select_proveedor import ControladorSelectProveedor
from controlador.select_libro import ControladorSelectLibro
from controlador.negocio import ControladorNegocio
from modelo.ranura_factura import RanuraFactura
from modelo.gestor_libro import GestorLibro
from modelo.gestor_factura import GestorFactura


class ControladorAbastecimiento(ControladorNegocio):
    def __init__(self):
        super().__init__()
        self.window.setWindowTitle("Nuevo abastecimiento")

    def finalizar(self):
        total = self.factura.total()
        if total > GestorLibro.caja:
            QMessageBox.critical(
                self.window,
                "Sistema gestión librería",
                "No hay suficiente dinero para realizar esta compra",
            )
            return
        for ranura_factura in self.factura.detalle:
            GestorLibro.abastecer(
                GestorLibro.index(ranura_factura.isbn),
                ranura_factura.cantidad,
                self.factura.fecha,
            )
        GestorLibro.caja -= total
        GestorFactura.agregar(self.factura)
        return super().finalizar()

    def libro_seleccionado(self, event):
        tabla = self.c.window.ui.tbl_libros
        if tabla.currentRow() == -1:
            return

        isbn = int(tabla.item(tabla.currentRow(), 0).text())
        try:
            self.factura.index(isbn)
            QMessageBox.critical(
                self.c.window,
                "Sistema gestión librería",
                "El libro ya se encuentra en la factura.",
            )
            return
        except ValueError:
            pass

        cantidad, ok = QInputDialog.getInt(
            self.c.window,
            "Sistema gestión librería",
            "Ingrese la cantidad a abastecer del libro seleccionado",
        )
        if not ok:
            return

        if cantidad <= 0:
            QMessageBox.critical(
                self.c.window,
                "Sistema gestión librería",
                "Ingrese una cantidad válida.",
            )
            return

        self.factura.agre_item(
            RanuraFactura(
                isbn,
                cantidad,
                float(tabla.item(tabla.currentRow(), 2).text()),
            )
        )
        return super().libro_seleccionado(event)

    def select_usuario(self, event):
        if event.button() != Qt.MouseButton.LeftButton:
            return
        self.c = ControladorSelectProveedor()
        self.c.window.closeEvent = self.usuario_seleccionado

    def agregar(self):
        self.c = ControladorSelectLibro(1)
        self.c.window.closeEvent = self.libro_seleccionado
