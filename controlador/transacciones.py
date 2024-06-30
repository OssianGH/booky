from PyQt6.QtWidgets import QTableWidgetItem
from modelo.transaccion import Transaccion
from modelo.tools import ReadOnlyDelegate
from vista.transacciones import VentanaTransacciones


class ControladorTransacciones:
    def __init__(self, libro):
        self.window = VentanaTransacciones()
        self.libro = libro
        self.window.ui.btn_cerrar.clicked.connect(lambda: self.window.close())
        self.window.ui.cmb_criterio.currentIndexChanged.connect(
            lambda: self.cargar_tabla()
        )
        self.setup_combo()
        self.setup_tabla()
        self.cargar_tabla()

    def setup_combo(self):
        self.window.ui.cmb_criterio.addItems(
            ["Todas", Transaccion.Tipo.abastecimiento, Transaccion.Tipo.venta]
        )

    def setup_tabla(self):
        tabla = self.window.ui.tbl_transacciones
        tabla.setColumnCount(3)
        tabla.setHorizontalHeaderLabels(["FECHA", "TIPO", "CANTIDAD"])

    def cargar_tabla(self):
        vista = self.window.ui
        tabla = vista.tbl_transacciones
        tabla.clearContents()
        tabla.setRowCount(0)
        for transaccion in self.libro.l_transacciones(
            self.parse_criterio(vista.cmb_criterio.currentText())
        ):
            row_position = tabla.rowCount()
            tabla.insertRow(row_position)
            tabla.setItemDelegateForRow(row_position, ReadOnlyDelegate(self.window))
            tabla.setItem(
                row_position,
                0,
                QTableWidgetItem(transaccion.fecha.strftime("%d/%m/%Y")),
            )
            tabla.setItem(row_position, 1, QTableWidgetItem(transaccion.tipo))
            tabla.setItem(row_position, 2, QTableWidgetItem(str(transaccion.cantidad)))

    @staticmethod
    def parse_criterio(texto):
        if texto == "Todas":
            return ""
        return texto
