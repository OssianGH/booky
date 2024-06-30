from PyQt6.QtWidgets import QTableWidgetItem
from controlador.select_usuario import ControladorSelectUsuario
from modelo.gestor_usuario import GestorUsuario
from modelo.tools import ReadOnlyDelegate


class ControladorSelectProveedor(ControladorSelectUsuario):
    def __init__(self):
        super().__init__()
        self.window.setWindowTitle("Seleccionar proveedor para los datos de la factura")

    def cargar_tabla(self):
        vista = self.window.ui
        tabla = vista.tbl_usuarios
        tabla.clearContents()
        tabla.setRowCount(0)
        for cliente in GestorUsuario.proveedores(vista.txt_cedula.text()):
            row_position = tabla.rowCount()
            tabla.insertRow(row_position)
            tabla.setItemDelegateForRow(row_position, ReadOnlyDelegate(self.window))
            tabla.setItem(row_position, 0, QTableWidgetItem(cliente.cedula))
            tabla.setItem(row_position, 1, QTableWidgetItem(cliente.nombre))
            tabla.setItem(row_position, 2, QTableWidgetItem(cliente.direccion))
            tabla.setItem(row_position, 3, QTableWidgetItem(cliente.telefono))
            tabla.setItem(row_position, 4, QTableWidgetItem(cliente.correo))
