from PyQt6.QtWidgets import QMessageBox, QFileDialog
from PyQt6.QtGui import QPixmap
from modelo.gestor_libro import GestorLibro
from modelo.tools import Validador
from vista.alterar_libro import VentanaAlterarLibro
from os.path import basename, join
from shutil import copyfile


class ControladorAlterarLibro:
    def __init__(self):
        self.ruta = "./resources/sin_portada.png"
        self.window = VentanaAlterarLibro()
        self.window.ui.btn_aceptar.clicked.connect(lambda: self.aceptar())
        self.window.ui.btn_cancelar.clicked.connect(lambda: self.window.close())
        self.window.ui.btn_imagen.clicked.connect(lambda: self.imagen())
        self.window.ui.txt_titulo.textChanged.connect(lambda: self.validar_grabar())
        self.window.ui.txt_p_compra.textChanged.connect(lambda: self.validar_grabar())
        self.window.ui.txt_p_venta.textChanged.connect(lambda: self.validar_grabar())
        self.window.ui.txt_titulo.setValidator(Validador.letras_enteros)
        self.window.ui.txt_p_compra.setValidator(Validador.decimales)
        self.window.ui.txt_p_venta.setValidator(Validador.decimales)
        self.window.ui.txt_isbn.setEnabled(False)

    def validar_grabar(self):
        self.window.ui.btn_aceptar.setEnabled(
            len(self.window.ui.txt_titulo.text()) != 0
            and len(self.window.ui.txt_p_compra.text()) != 0
            and len(self.window.ui.txt_p_venta.text()) != 0
        )

    def aceptar(self):
        GestorLibro.grabar_datos()
        self.window.close()

    def imagen(self):
        origen = QFileDialog.getOpenFileName(
            self.window,
            "Selecciona una imagen",
            "C:/users",
            "Image Files (*.png *.jpg *.bmp)",
        )[0]
        destino = join("./resources", basename(origen))
        try:
            copyfile(origen, destino)
        except FileNotFoundError:
            QMessageBox.critical(
                self.window, "Sistema gestión librería", "No se encuentra el archivo"
            )
            return
        self.window.ui.lbl_imagen.setPixmap(QPixmap(destino))
        self.ruta = destino
