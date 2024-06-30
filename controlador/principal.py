from PyQt6.QtWidgets import QTableWidgetItem, QApplication, QMessageBox
from PyQt6.QtCore import QEasingCurve, QPropertyAnimation
from controlador.agregar_cliente import ControladorAgregarCliente
from controlador.agregar_libro import ControladorAgregarLibro
from controlador.agregar_proveedor import ControladorAgregarProveedor
from controlador.detalle import ControladorDetalle
from controlador.editar_libro import ControladorEditarLibro
from controlador.editar_usuario import ControladorEditarUsuario
from controlador.venta import ControladorVenta
from controlador.transacciones import ControladorTransacciones
from controlador.ver_libro import ControladorVerLibro
from controlador.abastecimiento import ControladorAbastecimiento
from modelo.gestor_factura import GestorFactura
from modelo.gestor_libro import GestorLibro
from modelo.gestor_usuario import GestorUsuario
from modelo.libro import Libro
from modelo.tools import Validador, ReadOnlyDelegate, ImageWidget
from sys import argv
from vista.principal import VentanaPrincipal


class ControladorPrincipal:
    def __init__(self):
        self.app = QApplication(argv)
        self.window = VentanaPrincipal()
        self.window.ui.btn_toggle.clicked.connect(lambda: self.toogle_menu())
        self.window.ui.btn_home.clicked.connect(lambda: self.inicio_pagina())
        self.window.ui.btn_libros.clicked.connect(lambda: self.libros_pagina())
        self.window.ui.btn_clientes.clicked.connect(lambda: self.clientes_pagina())
        self.window.ui.btn_proveedores.clicked.connect(
            lambda: self.proveedores_pagina()
        )
        self.window.ui.btn_facturas.clicked.connect(lambda: self.facturas_pagina())
        self.window.ui.btn_cerrar.clicked.connect(lambda: self.window.close())
        self.window.ui.btn_economico.clicked.connect(lambda: self.mas_economico())
        self.window.ui.btn_costoso.clicked.connect(lambda: self.mas_costoso())
        self.window.ui.btn_vendido.clicked.connect(lambda: self.mas_vendido())

        self.window.pagina_home.ui.btn_vender.clicked.connect(
            lambda: self.inicio_vender()
        )
        self.window.pagina_home.ui.btn_abastecer.clicked.connect(
            lambda: self.inicio_abastecer()
        )

        self.window.pagina_libros.ui.btn_nuevo.clicked.connect(
            lambda: self.libros_nuevo()
        )
        self.window.pagina_libros.ui.btn_editar.clicked.connect(
            lambda: self.libros_editar()
        )
        self.window.pagina_libros.ui.btn_eliminar.clicked.connect(
            lambda: self.libros_eliminar()
        )
        self.window.pagina_libros.ui.btn_transacciones.clicked.connect(
            lambda: self.libros_transacciones()
        )
        self.window.pagina_libros.ui.txt_query.textChanged.connect(
            lambda: self.libros_cargar_tabla()
        )
        self.window.pagina_libros.ui.btn_editar.setEnabled(False)
        self.window.pagina_libros.ui.btn_eliminar.setEnabled(False)
        self.window.pagina_libros.ui.btn_transacciones.setEnabled(False)

        self.window.pagina_clientes.ui.btn_nuevo.clicked.connect(
            lambda: self.clientes_nuevo()
        )
        self.window.pagina_clientes.ui.btn_editar.clicked.connect(
            lambda: self.clientes_editar()
        )
        self.window.pagina_clientes.ui.btn_eliminar.clicked.connect(
            lambda: self.clientes_eliminar()
        )
        self.window.pagina_clientes.ui.txt_query.textChanged.connect(
            lambda: self.clientes_cargar_tabla()
        )
        self.window.pagina_clientes.ui.txt_query.setValidator(Validador.enteros)
        self.window.pagina_clientes.ui.btn_editar.setEnabled(False)
        self.window.pagina_clientes.ui.btn_eliminar.setEnabled(False)

        self.window.pagina_proveedores.ui.btn_nuevo.clicked.connect(
            lambda: self.proveedores_nuevo()
        )
        self.window.pagina_proveedores.ui.btn_editar.clicked.connect(
            lambda: self.proveedores_editar()
        )
        self.window.pagina_proveedores.ui.btn_eliminar.clicked.connect(
            lambda: self.proveedores_eliminar()
        )
        self.window.pagina_proveedores.ui.txt_query.textChanged.connect(
            lambda: self.proveedores_cargar_tabla()
        )
        self.window.pagina_clientes.ui.txt_query.setValidator(Validador.enteros)
        self.window.pagina_proveedores.ui.btn_editar.setEnabled(False)
        self.window.pagina_proveedores.ui.btn_eliminar.setEnabled(False)

        self.window.pagina_facturas.ui.btn_detalle.clicked.connect(
            lambda: self.facturas_detalle()
        )
        self.window.pagina_facturas.ui.btn_detalle.setEnabled(False)

        GestorLibro.cargar_datos()
        GestorFactura.cargar_datos()
        GestorUsuario.cargar_datos()
        self.window.pagina_home.ui.lbl_caja_valor.setText(str(GestorLibro.caja))
        self.libros_setup_combo()
        self.libros_setup_tabla()
        self.clientes_setup_tabla()
        self.proveedores_setup_tabla()
        self.facturas_setup_tabla()

    def inicio_vender(self):
        if len(GestorLibro.libros_vendibles()) == 0:
            QMessageBox.critical(
                self.window,
                "Sistema gestión librería",
                "No hay libros en el almacen que se puedan vender, "
                + "todos tienen stock = 0.\n"
                + "Puede abastecer libros en esta misma pestaña",
            )
            return
        self.c = ControladorVenta()
        self.c.window.closeEvent = self.actualizacion_caja

    def inicio_abastecer(self):
        if len(GestorLibro.libros) == 0:
            return QMessageBox.critical(
                self.window, "Sistema gestión librería", "No hay libros registrados"
            )
        self.c = ControladorAbastecimiento()
        self.c.window.closeEvent = self.actualizacion_caja

    def actualizacion_caja(self, event):
        self.window.pagina_home.ui.lbl_caja_valor.setText(str(GestorLibro.caja))

    def inicio_pagina(self):
        self.window.pagina_home.ui.lbl_caja_valor.setText(str(GestorLibro.caja))
        self.window.ui.stk_paginas.setCurrentWidget(self.window.pagina_home)

    def libros_setup_combo(self):
        self.window.pagina_libros.ui.cmb_criterio.addItems(
            [Libro.Criterio.isbn, Libro.Criterio.titulo]
        )

    def libros_setup_tabla(self):
        tabla = self.window.pagina_libros.ui.tbl_libros
        tabla.setColumnCount(6)
        tabla.setHorizontalHeaderLabels(
            ["ISBN", "TÍTULO", "PRECIO COMPRA", "PRECIO VENTA", "UNIDADES", "PORTADA"]
        )

    def libros_cargar_tabla(self):
        vista = self.window.pagina_libros.ui
        tabla = vista.tbl_libros
        tabla.clearContents()
        tabla.setRowCount(0)
        if vista.cmb_criterio.currentText() == Libro.Criterio.isbn:
            libros = GestorLibro.libros_isbn(vista.txt_query.text().strip())
        elif vista.cmb_criterio.currentText() == Libro.Criterio.titulo:
            libros = GestorLibro.libros_titulo(vista.txt_query.text().strip())
        for libro in libros:
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

    def libros_nuevo(self):
        self.c = ControladorAgregarLibro()
        self.c.window.closeEvent = self.libros_actualizar_evento

    def libros_editar(self):
        vista = self.window.pagina_libros.ui
        tabla = vista.tbl_libros
        try:
            index = GestorLibro.index(int(tabla.item(tabla.currentRow(), 0).text()))
        except ValueError as e:
            QMessageBox.critical(self.window, "Sistema gestión librería", str(e))
            return
        except AttributeError as e:
            QMessageBox.critical(self.window, "Sistema gestión librería", str(e))
            return
        libro = GestorLibro.libros[index]
        self.c = ControladorEditarLibro(libro)
        self.c.window.closeEvent = self.libros_actualizar_evento

    def libros_eliminar(self):
        vista = self.window.pagina_libros.ui
        tabla = vista.tbl_libros
        try:
            index = GestorLibro.index(int(tabla.item(tabla.currentRow(), 0).text()))
        except ValueError as e:
            QMessageBox.critical(self.window, "Sistema gestión librería", str(e))
            return
        except AttributeError as e:
            QMessageBox.critical(self.window, "Sistema gestión librería", str(e))
            return
        m = QMessageBox.question(
            self.window, "Sistema gestión librería", "¿Está seguro de eliminar?"
        )
        if m == QMessageBox.StandardButton.Yes:
            GestorLibro.eliminar(index)
            GestorLibro.grabar_datos()
            QMessageBox.information(
                self.window, "Sistema gestión librería", "Libro eliminado."
            )
            self.libros_actualizar()

    def libros_transacciones(self):
        vista = self.window.pagina_libros.ui
        tabla = vista.tbl_libros
        try:
            index = GestorLibro.index(int(tabla.item(tabla.currentRow(), 0).text()))
        except ValueError as e:
            QMessageBox.critical(self.window, "Sistema gestión librería", str(e))
            return
        except AttributeError as e:
            QMessageBox.critical(self.window, "Sistema gestión librería", str(e))
            return
        libro = GestorLibro.libros[index]
        self.c = ControladorTransacciones(libro)

    def libros_actualizar(self):
        vista = self.window.pagina_libros.ui
        vista.btn_editar.setEnabled(False)
        vista.btn_eliminar.setEnabled(False)
        vista.btn_transacciones.setEnabled(False)
        vista.txt_query.setText("")
        self.libros_cargar_tabla()

    def libros_actualizar_evento(self, event):
        self.libros_actualizar()

    def libros_pagina(self):
        self.libros_actualizar()
        self.window.ui.stk_paginas.setCurrentWidget(self.window.pagina_libros)

    def clientes_setup_tabla(self):
        tabla = self.window.pagina_clientes.ui.tbl_usuarios
        tabla.setColumnCount(5)
        tabla.setHorizontalHeaderLabels(
            ["CÉDULA", "NOMBRE", "DIRECCIÓN", "TELÉFONO", "CORREO"]
        )

    def clientes_cargar_tabla(self):
        vista = self.window.pagina_clientes.ui
        tabla = vista.tbl_usuarios
        tabla.clearContents()
        tabla.setRowCount(0)
        for cliente in GestorUsuario.clientes(vista.txt_query.text()):
            row_position = tabla.rowCount()
            tabla.insertRow(row_position)
            tabla.setItemDelegateForRow(row_position, ReadOnlyDelegate(self.window))
            tabla.setItem(row_position, 0, QTableWidgetItem(cliente.cedula))
            tabla.setItem(row_position, 1, QTableWidgetItem(cliente.nombre))
            tabla.setItem(row_position, 2, QTableWidgetItem(cliente.direccion))
            tabla.setItem(row_position, 3, QTableWidgetItem(cliente.telefono))
            tabla.setItem(row_position, 4, QTableWidgetItem(cliente.correo))

    def clientes_nuevo(self):
        self.c = ControladorAgregarCliente()
        self.c.window.closeEvent = self.clientes_actualizar_evento

    def clientes_editar(self):
        vista = self.window.pagina_clientes.ui
        tabla = vista.tbl_usuarios
        try:
            index = GestorUsuario.index(tabla.item(tabla.currentRow(), 0).text())
        except ValueError as e:
            QMessageBox.critical(self.window, "Sistema gestión librería", str(e))
            return
        except AttributeError as e:
            QMessageBox.critical(self.window, "Sistema gestión librería", str(e))
            return
        cliente = GestorUsuario.usuarios[index]
        self.c = ControladorEditarUsuario(cliente)
        self.c.window.closeEvent = self.clientes_actualizar_evento

    def clientes_eliminar(self):
        vista = self.window.pagina_clientes.ui
        tabla = vista.tbl_usuarios
        try:
            index = GestorUsuario.index(tabla.item(tabla.currentRow(), 0).text())
        except ValueError as e:
            QMessageBox.critical(self.window, "Sistema gestión librería", str(e))
            return
        except AttributeError as e:
            QMessageBox.critical(self.window, "Sistema gestión librería", str(e))
            return
        m = QMessageBox.question(
            self.window, "Sistema gestión librería", "¿Está seguro de eliminar?"
        )
        if m == QMessageBox.StandardButton.Yes:
            GestorUsuario.eliminar(index)
            GestorUsuario.grabar_datos()
            QMessageBox.information(
                self.window, "Sistema gestión librería", "Cliente eliminado."
            )
            self.clientes_actualizar()

    def clientes_actualizar(self):
        vista = self.window.pagina_clientes.ui
        vista.btn_editar.setEnabled(False)
        vista.btn_eliminar.setEnabled(False)
        vista.txt_query.setText("")
        self.clientes_cargar_tabla()

    def clientes_actualizar_evento(self, event):
        self.clientes_actualizar()

    def clientes_pagina(self):
        self.clientes_actualizar()
        self.window.ui.stk_paginas.setCurrentWidget(self.window.pagina_clientes)

    def proveedores_setup_tabla(self):
        tabla = self.window.pagina_proveedores.ui.tbl_usuarios
        tabla.setColumnCount(5)
        tabla.setHorizontalHeaderLabels(
            ["CÉDULA", "NOMBRE", "DIRECCIÓN", "TELÉFONO", "CORREO"]
        )

    def proveedores_cargar_tabla(self):
        vista = self.window.pagina_proveedores.ui
        tabla = vista.tbl_usuarios
        tabla.clearContents()
        tabla.setRowCount(0)
        for cliente in GestorUsuario.proveedores(vista.txt_query.text()):
            row_position = tabla.rowCount()
            tabla.insertRow(row_position)
            tabla.setItemDelegateForRow(row_position, ReadOnlyDelegate(self.window))
            tabla.setItem(row_position, 0, QTableWidgetItem(cliente.cedula))
            tabla.setItem(row_position, 1, QTableWidgetItem(cliente.nombre))
            tabla.setItem(row_position, 2, QTableWidgetItem(cliente.direccion))
            tabla.setItem(row_position, 3, QTableWidgetItem(cliente.telefono))
            tabla.setItem(row_position, 4, QTableWidgetItem(cliente.correo))

    def proveedores_nuevo(self):
        self.c = ControladorAgregarProveedor()
        self.c.window.closeEvent = self.proveedores_actualizar_evento

    def proveedores_editar(self):
        vista = self.window.pagina_proveedores.ui
        tabla = vista.tbl_usuarios
        try:
            index = GestorUsuario.index(tabla.item(tabla.currentRow(), 0).text())
        except ValueError as e:
            QMessageBox.critical(self.window, "Sistema gestión librería", str(e))
            return
        except AttributeError as e:
            QMessageBox.critical(self.window, "Sistema gestión librería", str(e))
            return
        proveedor = GestorUsuario.usuarios[index]
        self.c = ControladorEditarUsuario(proveedor)
        self.c.window.closeEvent = self.proveedores_actualizar_evento

    def proveedores_eliminar(self):
        vista = self.window.pagina_proveedores.ui
        tabla = vista.tbl_usuarios
        try:
            index = GestorUsuario.index(tabla.item(tabla.currentRow(), 0).text())
        except ValueError as e:
            QMessageBox.critical(self.window, "Sistema gestión librería", str(e))
            return
        except AttributeError as e:
            QMessageBox.critical(self.window, "Sistema gestión librería", str(e))
            return
        m = QMessageBox.question(
            self.window, "Sistema gestión librería", "¿Está seguro de eliminar?"
        )
        if m == QMessageBox.StandardButton.Yes:
            GestorUsuario.eliminar(index)
            GestorUsuario.grabar_datos()
            QMessageBox.information(
                self.window, "Sistema gestión librería", "Proveedor eliminado."
            )
            self.proveedores_actualizar()

    def proveedores_actualizar(self):
        vista = self.window.pagina_proveedores.ui
        vista.btn_editar.setEnabled(False)
        vista.btn_eliminar.setEnabled(False)
        vista.txt_query.setText("")
        self.proveedores_cargar_tabla()

    def proveedores_actualizar_evento(self, event):
        self.proveedores_actualizar()

    def proveedores_pagina(self):
        self.proveedores_actualizar()
        self.window.ui.stk_paginas.setCurrentWidget(self.window.pagina_proveedores)

    def facturas_setup_tabla(self):
        tabla = self.window.pagina_facturas.ui.tbl_facturas
        tabla.setColumnCount(4)
        tabla.setHorizontalHeaderLabels(["CÉDULA", "FECHA", "FORMA DE PAGO", "TOTAL"])

    def facturas_cargar_tabla(self):
        vista = self.window.pagina_facturas.ui
        tabla = vista.tbl_facturas
        tabla.clearContents()
        tabla.setRowCount(0)
        for factura in GestorFactura.facturas:
            row_position = tabla.rowCount()
            tabla.insertRow(row_position)
            tabla.setItemDelegateForRow(row_position, ReadOnlyDelegate(self.window))
            tabla.setItem(row_position, 0, QTableWidgetItem(factura.cedula))
            tabla.setItem(
                row_position, 1, QTableWidgetItem(factura.fecha.strftime("%d/%m/%Y"))
            )
            tabla.setItem(row_position, 2, QTableWidgetItem(factura.forma_pago))
            tabla.setItem(row_position, 3, QTableWidgetItem(str(factura.total())))

    def facturas_detalle(self):
        vista = self.window.pagina_facturas.ui
        try:
            index = GestorFactura.index(vista.tbl_facturas.currentRow() + 1)
        except ValueError as e:
            QMessageBox.critical(self.window, "Sistema gestión librería", str(e))
            return
        except ArithmeticError as e:
            QMessageBox.critical(self.window, "Sistema gestión librería", str(e))
            return
        factura = GestorFactura.facturas[index]
        self.c = ControladorDetalle(factura)

    def facturas_pagina(self):
        self.facturas_cargar_tabla()
        self.window.ui.stk_paginas.setCurrentWidget(self.window.pagina_facturas)

    def mas_economico(self):
        if len(GestorLibro.libros) == 0:
            return QMessageBox.critical(
                self.window, "Sistema gestión librería", "No hay libros registrados"
            )
        self.c = ControladorVerLibro(GestorLibro.menos_costoso(), "Libro más económico")

    def mas_costoso(self):
        if len(GestorLibro.libros) == 0:
            return QMessageBox.critical(
                self.window, "Sistema gestión librería", "No hay libros registrados"
            )
        self.c = ControladorVerLibro(GestorLibro.mas_costoso(), "Libro más costoso")

    def mas_vendido(self):
        if len(GestorLibro.libros) == 0:
            return QMessageBox.critical(
                self.window, "Sistema gestión librería", "No hay libros registrados"
            )
        self.c = ControladorVerLibro(GestorLibro.mas_vendido(), "Libro más vendido")

    def toogle_menu(self):
        width = self.window.ui.fra_barra_lateral.width()
        widthExtended = 70

        if width == 70:
            widthExtended = 200
        else:
            self.window.ui.btn_home.setText("")
            self.window.ui.btn_libros.setText("")
            self.window.ui.btn_clientes.setText("")
            self.window.ui.btn_proveedores.setText("")
            self.window.ui.btn_facturas.setText("")
            self.window.ui.btn_costoso.setText("")
            self.window.ui.btn_economico.setText("")
            self.window.ui.btn_vendido.setText("")

        self.animation = QPropertyAnimation()
        self.animation.finished.connect(lambda: self.toggle_menu_text())
        self.animation.setTargetObject(self.window.ui.fra_barra_lateral)
        self.animation.setPropertyName(b"minimumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animation.start()

    def toggle_menu_text(self):
        if self.window.ui.fra_barra_lateral.width() == 200:
            self.window.ui.btn_home.setText("  Inicio")
            self.window.ui.btn_libros.setText("  Libros")
            self.window.ui.btn_clientes.setText("  Clientes")
            self.window.ui.btn_proveedores.setText("  Proveedores")
            self.window.ui.btn_facturas.setText("  Facturas")
            self.window.ui.btn_costoso.setText("  Más costoso")
            self.window.ui.btn_economico.setText("  Más económico")
            self.window.ui.btn_vendido.setText("  Más vendido")
