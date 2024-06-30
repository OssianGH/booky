from vista.alterar_usuario import VentanaAlterarUsuario
from modelo.tools import Validador
from modelo.gestor_usuario import GestorUsuario


class ControladorAlterarUsuario:
    def __init__(self):
        self.window = VentanaAlterarUsuario()
        self.window.ui.btn_aceptar.clicked.connect(lambda: self.aceptar())
        self.window.ui.btn_cancelar.clicked.connect(lambda: self.window.close())
        self.window.ui.txt_cedula.textChanged.connect(lambda: self.validar_grabar())
        self.window.ui.txt_nombre.textChanged.connect(lambda: self.validar_grabar())
        self.window.ui.txt_direccion.textChanged.connect(lambda: self.validar_grabar())
        self.window.ui.txt_telefono.textChanged.connect(lambda: self.validar_grabar())
        self.window.ui.txt_correo.textChanged.connect(lambda: self.validar_grabar())
        self.window.ui.txt_cedula.setValidator(Validador.enteros)
        self.window.ui.txt_nombre.setValidator(Validador.letras)
        self.window.ui.txt_direccion.setValidator(Validador.letras_enteros)
        self.window.ui.txt_telefono.setValidator(Validador.enteros)
        self.window.ui.txt_correo.setValidator(Validador.correo)
        self.window.ui.btn_aceptar.setEnabled(False)

    def validar_grabar(self):
        self.window.ui.btn_aceptar.setEnabled(
            len(self.window.ui.txt_cedula.text()) != 0
            and len(self.window.ui.txt_nombre.text()) != 0
            and len(self.window.ui.txt_direccion.text()) != 0
            and len(self.window.ui.txt_telefono.text()) != 0
            and len(self.window.ui.txt_correo.text()) != 0
        )

    def aceptar(self):
        GestorUsuario.grabar_datos()
        self.window.close()
