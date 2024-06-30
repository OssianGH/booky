from PyQt6.QtWidgets import QTableWidgetItem
from modelo.gestor_usuario import GestorUsuario
from modelo.tools import Validador, ReadOnlyDelegate
from vista.select_usuario import VentanaSelectUsuario


class ControladorSelectUsuario:
    def __init__(self):
        self.window = VentanaSelectUsuario()
        self.window.ui.btn_cerrar.clicked.connect(lambda: self.window.close())
        self.window.ui.txt_cedula.textChanged.connect(lambda: self.cargar_tabla())
        self.window.ui.txt_cedula.setValidator(Validador.enteros)
        self.setup_tabla()
        self.cargar_tabla()

    def setup_tabla(self):
        tabla = self.window.ui.tbl_usuarios
        tabla.setColumnCount(5)
        tabla.setHorizontalHeaderLabels(
            ["CÉDULA", "NOMBRE", "DIRECCIÓN", "TELÉFONO", "CORREO"]
        )

    def cargar_tabla(self):
        vista = self.window.ui
        tabla = vista.tbl_usuarios
        tabla.clearContents()
        tabla.setRowCount(0)
        for cliente in GestorUsuario.l_usuarios(vista.txt_cedula.text()):
            row_position = tabla.rowCount()
            tabla.insertRow(row_position)
            tabla.setItemDelegateForRow(row_position, ReadOnlyDelegate(self.window))
            tabla.setItem(row_position, 0, QTableWidgetItem(cliente.cedula))
            tabla.setItem(row_position, 1, QTableWidgetItem(cliente.nombre))
            tabla.setItem(row_position, 2, QTableWidgetItem(cliente.direccion))
            tabla.setItem(row_position, 3, QTableWidgetItem(cliente.telefono))
            tabla.setItem(row_position, 4, QTableWidgetItem(cliente.correo))
