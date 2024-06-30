from PyQt6.QtGui import QPixmap
from vista.ver_libro import VentanaVerLibro


class ControladorVerLibro:
    def __init__(self, libro, text):
        self.window = VentanaVerLibro()
        self.window.setWindowTitle(text)
        self.window.ui.txt_isbn.setText(str(libro.isbn))
        self.window.ui.txt_titulo.setText(libro.titulo)
        self.window.ui.txt_p_compra.setText(str(libro.precio_compra))
        self.window.ui.txt_p_venta.setText(str(libro.precio_venta))
        self.window.ui.txt_cantidad.setText(str(libro.stock))
        self.window.ui.lbl_imagen.setPixmap(QPixmap(libro.ruta_imagen))
