from PyQt6.QtWidgets import QTableWidgetItem
from modelo.gestor_libro import GestorLibro
from modelo.tools import Validador, ReadOnlyDelegate, ImageWidget
from vista.select_libro import VentanaSelectLibro


class ControladorSelectLibro:
    def __init__(self, tipo):
        self.tipo = tipo
        self.window = VentanaSelectLibro()
        self.window.ui.btn_cerrar.clicked.connect(lambda: self.window.close())
        self.window.ui.txt_isbn.textChanged.connect(lambda: self.cargar_tabla())
        self.window.ui.txt_isbn.setValidator(Validador.enteros)
        self.setup_tabla()
        self.cargar_tabla()

    def setup_tabla(self):
        tabla = self.window.ui.tbl_libros
        tabla.setColumnCount(6)
        tabla.setHorizontalHeaderLabels(
            ["ISBN", "TÍTULO", "PRECIO COMPRA", "PRECIO VENTA", "UNIDADES", "PORTADA"]
        )

    def cargar_tabla(self):
        vista = self.window.ui
        tabla = vista.tbl_libros
        tabla.clearContents()
        tabla.setRowCount(0)
        if self.tipo == 0:
            lista = GestorLibro.libros_vendibles(vista.txt_isbn.text())
        elif self.tipo == 1:
            lista = GestorLibro.libros_isbn(vista.txt_isbn.text())
        for libro in lista:
            row_position = tabla.rowCount()
            tabla.insertRow(row_position)
            tabla.setRowHeight(row_position, 180)
            tabla.setItemDelegateForRow(row_position, ReadOnlyDelegate(self.window))
            tabla.setItem(row_position, 0, QTableWidgetItem(str(libro.isbn)))
            tabla.setItem(row_position, 1, QTableWidgetItem(libro.titulo))
            tabla.setItem(row_position, 2, QTableWidgetItem(str(libro.precio_compra)))
            tabla.setItem(row_position, 3, QTableWidgetItem(str(libro.precio_venta)))
            tabla.setItem(row_position, 4, QTableWidgetItem(str(libro.stock)))
            tabla.setCellWidget(
                row_position, 5, ImageWidget(self.window, libro.ruta_imagen)
            )
