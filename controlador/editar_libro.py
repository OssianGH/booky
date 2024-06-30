from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QPixmap
from controlador.alterar_libro import ControladorAlterarLibro


class ControladorEditarLibro(ControladorAlterarLibro):
    def __init__(self, libro):
        super().__init__()
        self.libro = libro
        self.window.setWindowTitle("Editar libro")
        self.cargar_textos()
        self.window.ui.btn_aceptar.setEnabled(False)

    def cargar_textos(self):
        self.window.ui.txt_isbn.setText(str(self.libro.isbn))
        self.window.ui.txt_titulo.setText(self.libro.titulo)
        self.window.ui.txt_p_compra.setText(str(self.libro.precio_compra))
        self.window.ui.txt_p_venta.setText(str(self.libro.precio_venta))
        self.window.ui.lbl_imagen.setPixmap(QPixmap(self.libro.ruta_imagen))
        self.ruta = self.libro.ruta_imagen

    def aceptar(self):
        m = QMessageBox.question(
            self.window, "Sistema gestión librería", "¿Está seguro de editar?"
        )
        if m == QMessageBox.StandardButton.Yes:
            self.libro.titulo = self.window.ui.txt_titulo.text()
            self.libro.precio_compra = float(self.window.ui.txt_p_compra.text())
            self.libro.precio_venta = float(self.window.ui.txt_p_venta.text())
            self.libro.ruta_imagen = self.ruta
            QMessageBox.information(
                self.window, "Sistema gestión librería", "Libro editado."
            )
            return super().aceptar()

    def imagen(self):
        self.window.ui.btn_aceptar.setEnabled(True)
        return super().imagen()
