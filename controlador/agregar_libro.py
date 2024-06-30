from PyQt6.QtWidgets import QMessageBox
from controlador.alterar_libro import ControladorAlterarLibro
from modelo.gestor_libro import GestorLibro
from modelo.libro import Libro


class ControladorAgregarLibro(ControladorAlterarLibro):
    def __init__(self):
        super().__init__()
        self.window.setWindowTitle("Agregar libro")
        self.window.ui.txt_isbn.setText(GestorLibro.generar_isbn())
        self.window.ui.btn_aceptar.setEnabled(False)

    def aceptar(self):
        m = QMessageBox.question(
            self.window, "Sistema gestión librería", "¿Está seguro de agregar?"
        )
        if m == QMessageBox.StandardButton.Yes:
            libro = Libro(
                int(self.window.ui.txt_isbn.text()),
                self.window.ui.txt_titulo.text().strip(),
                float(self.window.ui.txt_p_compra.text()),
                float(self.window.ui.txt_p_venta.text()),
                0,
                self.ruta,
            )
            GestorLibro.agregar(libro)
            QMessageBox.information(
                self.window, "Sistema gestión librería", "Libro agregado."
            )
            return super().aceptar()
