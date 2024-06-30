from PyQt6.QtWidgets import QMessageBox
from controlador.alterar_usuario import ControladorAlterarUsuario
from modelo.gestor_usuario import GestorUsuario
from modelo.usuario import Usuario
from modelo.tools import cedula_valida


class ControladorAgregarProveedor(ControladorAlterarUsuario):
    def __init__(self):
        super().__init__()
        self.window.setWindowTitle("Agregar proveedor")
        self.window.ui.btn_aceptar.setEnabled(False)

    def aceptar(self):
        m = QMessageBox.question(
            self.window, "Sistema gestión librería", "¿Está seguro de agregar?"
        )
        if m == QMessageBox.StandardButton.Yes:
            cedula = self.window.ui.txt_cedula.text()
            if not cedula_valida(cedula):
                QMessageBox.critical(
                    self.window, "Sistema gestión librería", "La cédula no es válida"
                )
                return

            try:
                GestorUsuario.index(cedula)
                QMessageBox.critical(
                    self.window,
                    "Sistema gestión librería",
                    "Ya existe un usuario con dicha cédula",
                )
                return
            except ValueError:
                pass

            proveedor = Usuario(
                cedula,
                self.window.ui.txt_nombre.text().strip(),
                self.window.ui.txt_direccion.text(),
                self.window.ui.txt_telefono.text(),
                self.window.ui.txt_correo.text(),
                Usuario.Tipo.proveedor,
            )
            GestorUsuario.agregar(proveedor)
            QMessageBox.information(
                self.window, "Sistema gestión librería", "Proveedor agregado."
            )
            return super().aceptar()
