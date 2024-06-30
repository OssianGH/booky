from PyQt6.QtWidgets import QMessageBox
from controlador.alterar_usuario import ControladorAlterarUsuario
from modelo.usuario import Usuario


class ControladorEditarUsuario(ControladorAlterarUsuario):
    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario
        self.window.setWindowTitle(
            f"Editar {self.parse_tipo(self.usuario.tipo).lower()}"
        )
        self.cargar_textos()
        self.window.ui.btn_aceptar.setEnabled(False)
        self.window.ui.txt_cedula.setEnabled(False)

    def cargar_textos(self):
        self.window.ui.txt_cedula.setText(self.usuario.cedula)
        self.window.ui.txt_nombre.setText(self.usuario.nombre)
        self.window.ui.txt_direccion.setText(self.usuario.direccion)
        self.window.ui.txt_telefono.setText(self.usuario.telefono)
        self.window.ui.txt_correo.setText(self.usuario.correo)

    def aceptar(self):
        m = QMessageBox.question(
            self.window, "Sistema gestión librería", "¿Está seguro de editar?"
        )
        if m == QMessageBox.StandardButton.Yes:
            self.usuario.cedula = self.window.ui.txt_cedula.text()
            self.usuario.nombre = self.window.ui.txt_nombre.text()
            self.usuario.direccion = self.window.ui.txt_direccion.text()
            self.usuario.telefono = self.window.ui.txt_telefono.text()
            self.usuario.correo = self.window.ui.txt_correo.text()
            QMessageBox.information(
                self.window,
                "Sistema gestión librería",
                f"{self.parse_tipo(self.usuario.tipo)} editado.",
            )
            return super().aceptar()

    @staticmethod
    def parse_tipo(criterio):
        return {
            Usuario.Tipo.proveedor: "Proveedor",
            Usuario.Tipo.cliente: "Cliente",
        }.get(criterio)
