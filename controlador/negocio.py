from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem
from vista.negocio import VentanaNegocio
from modelo.tools import ReadOnlyDelegate
from modelo.gestor_usuario import GestorUsuario
from modelo.gestor_factura import GestorFactura
from modelo.gestor_libro import GestorLibro
from modelo.factura import Factura


class ControladorNegocio:
    def __init__(self):
        self.factura = None
        self.window = VentanaNegocio()
        self.window.ui.btn_continuar.clicked.connect(lambda: self.continuar())
        self.window.ui.btn_agregar.clicked.connect(lambda: self.agregar())
        self.window.ui.btn_eliminar.clicked.connect(lambda: self.eliminar())
        self.window.ui.btn_finalizar.clicked.connect(lambda: self.finalizar())
        self.window.ui.btn_c_cancelar.clicked.connect(lambda: self.cancelar())
        self.window.ui.btn_d_cancelar.clicked.connect(lambda: self.cancelar())
        self.window.ui.txt_cedula.textChanged.connect(lambda: self.validar_continuar())
        self.window.ui.cmb_m_pago.currentIndexChanged.connect(
            lambda: self.validar_continuar()
        )
        self.window.ui.txt_cedula.mousePressEvent = self.select_usuario
        self.window.ui.txt_nombre.mousePressEvent = self.select_usuario
        self.window.ui.txt_direccion.mousePressEvent = self.select_usuario
        self.window.ui.txt_correo.mousePressEvent = self.select_usuario
        self.window.ui.txt_telefono.mousePressEvent = self.select_usuario
        self.setup_combo()
        self.setup_tabla()
        self.window.ui.btn_continuar.setEnabled(False)
        self.window.ui.btn_eliminar.setEnabled(False)
        self.window.ui.btn_finalizar.setEnabled(False)

    def setup_combo(self):
        combo = self.window.ui.cmb_m_pago
        combo.addItems(["Efectivo", "Tarjeta", "Cheque"])
        combo.setCurrentIndex(-1)

    def setup_tabla(self):
        tabla = self.window.ui.tbl_productos
        tabla.setColumnCount(3)
        tabla.setHorizontalHeaderLabels(["ISBN", "CANTIDAD", "PRECIO"])

    def cargar_tabla(self):
        vista = self.window.ui
        tabla = vista.tbl_productos
        tabla.clearContents()
        tabla.setRowCount(0)
        for linea_factura in self.factura.detalle:
            row_position = tabla.rowCount()
            tabla.insertRow(row_position)
            tabla.setItemDelegateForRow(row_position, ReadOnlyDelegate(self.window))
            tabla.setItem(row_position, 0, QTableWidgetItem(str(linea_factura.isbn)))
            tabla.setItem(
                row_position, 1, QTableWidgetItem(str(linea_factura.cantidad))
            )
            tabla.setItem(row_position, 2, QTableWidgetItem(str(linea_factura.precio)))

    def continuar(self):
        vista = self.window.ui
        self.window.ui.lbl_titulo.setText("Detalle de la factura")
        self.factura = Factura(
            GestorFactura.sig_val(),
            vista.txt_cedula.text(),
            vista.dte_fecha.date().toPyDate(),
            vista.cmb_m_pago.currentText(),
        )
        vista.stk_factura.setCurrentIndex(1)

    def agregar(self):
        pass

    def eliminar(self):
        vista = self.window.ui
        tabla = vista.tbl_productos
        try:
            index = self.factura.index(int(tabla.item(tabla.currentRow(), 0).text()))
            print(index)
        except ValueError:
            return
        except AttributeError:
            return
        m = QMessageBox.question(
            self.window,
            "Sistema gestión librería",
            "¿Está seguro de eliminar este item de la factura?",
        )
        if m == QMessageBox.StandardButton.Yes:
            self.factura.elim_item(index)
            self.cargar_tabla()
            self.window.ui.txt_total.setText(str(self.factura.total()))
            self.window.ui.btn_eliminar.setEnabled(False)
            if len(self.factura.detalle) == 0:
                self.window.ui.btn_finalizar.setEnabled(False)

    def finalizar(self):
        GestorLibro.grabar_datos()
        GestorFactura.grabar_datos()
        self.window.close()

    def cancelar(self):
        m = QMessageBox.question(
            self.window,
            "Sistema gestión librería",
            "¿Está seguro?\n\nSe cancelará toda la transacción.",
        )
        if m == QMessageBox.StandardButton.Yes:
            self.window.close()

    def libro_seleccionado(self, event):
        self.cargar_tabla()
        self.window.ui.txt_total.setText(str(self.factura.total()))
        self.window.ui.btn_finalizar.setEnabled(True)
        self.window.ui.btn_eliminar.setEnabled(False)

    def select_usuario(self, event):
        pass

    def usuario_seleccionado(self, event):
        tabla = self.c.window.ui.tbl_usuarios
        try:
            index = GestorUsuario.index(tabla.item(tabla.currentRow(), 0).text())
        except ValueError:
            return
        except AttributeError:
            return
        usuario = GestorUsuario.usuarios[index]

        self.window.ui.txt_cedula.setText(usuario.cedula)
        self.window.ui.txt_nombre.setText(usuario.nombre)
        self.window.ui.txt_direccion.setText(usuario.direccion)
        self.window.ui.txt_telefono.setText(usuario.telefono)
        self.window.ui.txt_correo.setText(usuario.correo)

    def validar_continuar(self):
        self.window.ui.btn_continuar.setEnabled(
            len(self.window.ui.txt_cedula.text()) != 0
            and self.window.ui.cmb_m_pago.currentIndex() != -1
        )
