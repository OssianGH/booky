from PyQt6.QtWidgets import QTableWidgetItem
from modelo.tools import ReadOnlyDelegate
from vista.detalle import VentanaDetalle


class ControladorDetalle:
    def __init__(self, factura):
        self.window = VentanaDetalle()
        self.factura = factura
        self.window.ui.btn_cerrar.clicked.connect(lambda: self.window.close())
        self.setup_tabla()
        self.cargar_tabla()

    def setup_tabla(self):
        tabla = self.window.ui.tbl_detalle
        tabla.setColumnCount(3)
        tabla.setHorizontalHeaderLabels(["ISBN", "CANTIDAD", "PRECIO"])

    def cargar_tabla(self):
        vista = self.window.ui
        tabla = vista.tbl_detalle
        tabla.clearContents()
        tabla.setRowCount(0)
        for ranura_factura in self.factura.detalle:
            row_position = tabla.rowCount()
            tabla.insertRow(row_position)
            tabla.setItemDelegateForRow(row_position, ReadOnlyDelegate(self.window))
            tabla.setItem(row_position, 0, QTableWidgetItem(str(ranura_factura.isbn)))
            tabla.setItem(
                row_position, 1, QTableWidgetItem(str(ranura_factura.cantidad))
            )
            tabla.setItem(row_position, 2, QTableWidgetItem(str(ranura_factura.precio)))
