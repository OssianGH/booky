from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_frm_negocio(object):
    def setupUi(self, frm_negocio):
        frm_negocio.setObjectName("frm_negocio")
        frm_negocio.resize(1366, 768)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        frm_negocio.setFont(font)
        frm_negocio.setStyleSheet(
            "color: rgb(255,255,255);\n" "background-color: rgb(77, 44, 128);"
        )
        self.verticalLayout = QtWidgets.QVBoxLayout(frm_negocio)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fra_titulo = QtWidgets.QFrame(frm_negocio)
        self.fra_titulo.setMaximumSize(QtCore.QSize(16777215, 40))
        self.fra_titulo.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_titulo.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_titulo.setObjectName("fra_titulo")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.fra_titulo)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.lbl_titulo = QtWidgets.QLabel(self.fra_titulo)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(14)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setStyleSheet("color: rgb(255,255,255);")
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.verticalLayout_9.addWidget(self.lbl_titulo)
        self.verticalLayout.addWidget(self.fra_titulo)
        self.fra_contenido = QtWidgets.QFrame(frm_negocio)
        self.fra_contenido.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_contenido.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_contenido.setObjectName("fra_contenido")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.fra_contenido)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stk_factura = QtWidgets.QStackedWidget(self.fra_contenido)
        self.stk_factura.setObjectName("stk_factura")
        self.wdg_cabecera = QtWidgets.QWidget()
        self.wdg_cabecera.setObjectName("wdg_cabecera")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.wdg_cabecera)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.fra_c_superior = QtWidgets.QFrame(self.wdg_cabecera)
        self.fra_c_superior.setStyleSheet("background-color: rgb(53, 28, 103);")
        self.fra_c_superior.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_c_superior.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_c_superior.setObjectName("fra_c_superior")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fra_c_superior)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fra_labels = QtWidgets.QFrame(self.fra_c_superior)
        self.fra_labels.setMaximumSize(QtCore.QSize(150, 16777215))
        self.fra_labels.setStyleSheet("background-color: rgb(53, 28, 103);")
        self.fra_labels.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_labels.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_labels.setObjectName("fra_labels")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fra_labels)
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_cedula = QtWidgets.QLabel(self.fra_labels)
        self.lbl_cedula.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_cedula.setFont(font)
        self.lbl_cedula.setObjectName("lbl_cedula")
        self.verticalLayout_3.addWidget(self.lbl_cedula)
        self.lbl_nombre = QtWidgets.QLabel(self.fra_labels)
        self.lbl_nombre.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.lbl_nombre.setFont(font)
        self.lbl_nombre.setStyleSheet("color: rgb(255,255,255);")
        self.lbl_nombre.setObjectName("lbl_nombre")
        self.verticalLayout_3.addWidget(self.lbl_nombre)
        self.lbl_direccion = QtWidgets.QLabel(self.fra_labels)
        self.lbl_direccion.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.lbl_direccion.setFont(font)
        self.lbl_direccion.setStyleSheet("color: rgb(255,255,255);")
        self.lbl_direccion.setObjectName("lbl_direccion")
        self.verticalLayout_3.addWidget(self.lbl_direccion)
        self.lbl_telefono = QtWidgets.QLabel(self.fra_labels)
        self.lbl_telefono.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.lbl_telefono.setFont(font)
        self.lbl_telefono.setStyleSheet("color: rgb(255,255,255);")
        self.lbl_telefono.setObjectName("lbl_telefono")
        self.verticalLayout_3.addWidget(self.lbl_telefono)
        self.lbl_correo = QtWidgets.QLabel(self.fra_labels)
        self.lbl_correo.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.lbl_correo.setFont(font)
        self.lbl_correo.setStyleSheet("color: rgb(255,255,255);")
        self.lbl_correo.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lbl_correo.setObjectName("lbl_correo")
        self.verticalLayout_3.addWidget(self.lbl_correo)
        self.lbl_m_pago = QtWidgets.QLabel(self.fra_labels)
        self.lbl_m_pago.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.lbl_m_pago.setFont(font)
        self.lbl_m_pago.setStyleSheet("color: rgb(255,255,255);")
        self.lbl_m_pago.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lbl_m_pago.setObjectName("lbl_m_pago")
        self.verticalLayout_3.addWidget(self.lbl_m_pago)
        self.lbl_fecha = QtWidgets.QLabel(self.fra_labels)
        self.lbl_fecha.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.lbl_fecha.setFont(font)
        self.lbl_fecha.setStyleSheet("color: rgb(255,255,255);")
        self.lbl_fecha.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lbl_fecha.setObjectName("lbl_fecha")
        self.verticalLayout_3.addWidget(self.lbl_fecha)
        self.horizontalLayout_2.addWidget(self.fra_labels)
        self.fra_lines = QtWidgets.QFrame(self.fra_c_superior)
        self.fra_lines.setStyleSheet("background-color: rgb(53, 28, 103);")
        self.fra_lines.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_lines.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_lines.setObjectName("fra_lines")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fra_lines)
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txt_cedula = QtWidgets.QLineEdit(self.fra_lines)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_cedula.sizePolicy().hasHeightForWidth())
        self.txt_cedula.setSizePolicy(sizePolicy)
        self.txt_cedula.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.txt_cedula.setFont(font)
        self.txt_cedula.setStyleSheet(
            "QLineEdit {\n"
            "    color: rgb(255,255,255);\n"
            "    background-color: rgb(77, 44, 128);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QLineEdit:disabled {\n"
            "    color: rgb(53, 28, 103);\n"
            "    background-color: rgb(103, 64, 153);\n"
            "}"
        )
        self.txt_cedula.setReadOnly(True)
        self.txt_cedula.setObjectName("txt_cedula")
        self.verticalLayout_2.addWidget(self.txt_cedula)
        self.txt_nombre = QtWidgets.QLineEdit(self.fra_lines)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_nombre.sizePolicy().hasHeightForWidth())
        self.txt_nombre.setSizePolicy(sizePolicy)
        self.txt_nombre.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.txt_nombre.setFont(font)
        self.txt_nombre.setStyleSheet(
            "QLineEdit {\n"
            "    color: rgb(255,255,255);\n"
            "    background-color: rgb(77, 44, 128);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QLineEdit:disabled {\n"
            "    color: rgb(53, 28, 103);\n"
            "    background-color: rgb(103, 64, 153);\n"
            "}"
        )
        self.txt_nombre.setReadOnly(True)
        self.txt_nombre.setObjectName("txt_nombre")
        self.verticalLayout_2.addWidget(self.txt_nombre)
        self.txt_direccion = QtWidgets.QLineEdit(self.fra_lines)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.txt_direccion.sizePolicy().hasHeightForWidth()
        )
        self.txt_direccion.setSizePolicy(sizePolicy)
        self.txt_direccion.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.txt_direccion.setFont(font)
        self.txt_direccion.setStyleSheet(
            "QLineEdit {\n"
            "    color: rgb(255,255,255);\n"
            "    background-color: rgb(77, 44, 128);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QLineEdit:disabled {\n"
            "    color: rgb(53, 28, 103);\n"
            "    background-color: rgb(103, 64, 153);\n"
            "}"
        )
        self.txt_direccion.setReadOnly(True)
        self.txt_direccion.setObjectName("txt_direccion")
        self.verticalLayout_2.addWidget(self.txt_direccion)
        self.txt_telefono = QtWidgets.QLineEdit(self.fra_lines)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_telefono.sizePolicy().hasHeightForWidth())
        self.txt_telefono.setSizePolicy(sizePolicy)
        self.txt_telefono.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.txt_telefono.setFont(font)
        self.txt_telefono.setStyleSheet(
            "QLineEdit {\n"
            "    color: rgb(255,255,255);\n"
            "    background-color: rgb(77, 44, 128);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QLineEdit:disabled {\n"
            "    color: rgb(53, 28, 103);\n"
            "    background-color: rgb(103, 64, 153);\n"
            "}"
        )
        self.txt_telefono.setReadOnly(True)
        self.txt_telefono.setObjectName("txt_telefono")
        self.verticalLayout_2.addWidget(self.txt_telefono)
        self.txt_correo = QtWidgets.QLineEdit(self.fra_lines)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_correo.sizePolicy().hasHeightForWidth())
        self.txt_correo.setSizePolicy(sizePolicy)
        self.txt_correo.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.txt_correo.setFont(font)
        self.txt_correo.setStyleSheet(
            "QLineEdit {\n"
            "    color: rgb(255,255,255);\n"
            "    background-color: rgb(77, 44, 128);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QLineEdit:disabled {\n"
            "    color: rgb(53, 28, 103);\n"
            "    background-color: rgb(103, 64, 153);\n"
            "}"
        )
        self.txt_correo.setReadOnly(True)
        self.txt_correo.setObjectName("txt_correo")
        self.verticalLayout_2.addWidget(self.txt_correo)
        self.cmb_m_pago = QtWidgets.QComboBox(self.fra_lines)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_m_pago.sizePolicy().hasHeightForWidth())
        self.cmb_m_pago.setSizePolicy(sizePolicy)
        self.cmb_m_pago.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.cmb_m_pago.setFont(font)
        self.cmb_m_pago.setStyleSheet(
            "color: rgb(255,255,255);\n"
            "    background-color: rgb(77, 44, 128);\n"
            "    border: 0px solid;"
        )
        self.cmb_m_pago.setObjectName("cmb_m_pago")
        self.verticalLayout_2.addWidget(self.cmb_m_pago)
        self.dte_fecha = QtWidgets.QDateEdit(self.fra_lines)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dte_fecha.sizePolicy().hasHeightForWidth())
        self.dte_fecha.setSizePolicy(sizePolicy)
        self.dte_fecha.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.dte_fecha.setFont(font)
        self.dte_fecha.setStyleSheet(
            "color: rgb(255,255,255);\n"
            "background-color: rgb(77, 44, 128);\n"
            "border: 0px solid;"
        )
        self.dte_fecha.setObjectName("dte_fecha")
        self.verticalLayout_2.addWidget(self.dte_fecha)
        self.horizontalLayout_2.addWidget(self.fra_lines)
        self.verticalLayout_7.addWidget(self.fra_c_superior)
        self.fra_c_inferior = QtWidgets.QFrame(self.wdg_cabecera)
        self.fra_c_inferior.setMaximumSize(QtCore.QSize(16777215, 30))
        self.fra_c_inferior.setStyleSheet("background-color: rgb(77, 44, 128);")
        self.fra_c_inferior.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_c_inferior.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_c_inferior.setObjectName("fra_c_inferior")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fra_c_inferior)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.fra_c_opciones = QtWidgets.QFrame(self.fra_c_inferior)
        self.fra_c_opciones.setStyleSheet("background-color: rgb(77, 44, 128);")
        self.fra_c_opciones.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_c_opciones.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_c_opciones.setObjectName("fra_c_opciones")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.fra_c_opciones)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_continuar = QtWidgets.QPushButton(self.fra_c_opciones)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_continuar.sizePolicy().hasHeightForWidth()
        )
        self.btn_continuar.setSizePolicy(sizePolicy)
        self.btn_continuar.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.btn_continuar.setFont(font)
        self.btn_continuar.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255,255,255);\n"
            "    background-color: rgb(53, 28, 103);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(103, 64, 153);\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "    background-color: rgb(103, 64, 153);\n"
            "    color: rgb(53, 28, 103);\n"
            "}"
        )
        self.btn_continuar.setObjectName("btn_continuar")
        self.horizontalLayout_3.addWidget(self.btn_continuar)
        self.btn_c_cancelar = QtWidgets.QPushButton(self.fra_c_opciones)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_c_cancelar.sizePolicy().hasHeightForWidth()
        )
        self.btn_c_cancelar.setSizePolicy(sizePolicy)
        self.btn_c_cancelar.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.btn_c_cancelar.setFont(font)
        self.btn_c_cancelar.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255,255,255);\n"
            "    background-color: rgb(53, 28, 103);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(103, 64, 153);\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "    background-color: rgb(103, 64, 153);\n"
            "    color: rgb(53, 28, 103);\n"
            "}"
        )
        self.btn_c_cancelar.setObjectName("btn_c_cancelar")
        self.horizontalLayout_3.addWidget(self.btn_c_cancelar)
        self.verticalLayout_5.addWidget(
            self.fra_c_opciones, 0, QtCore.Qt.AlignmentFlag.AlignRight
        )
        self.verticalLayout_7.addWidget(self.fra_c_inferior)
        self.stk_factura.addWidget(self.wdg_cabecera)
        self.wdg_detalle = QtWidgets.QWidget()
        self.wdg_detalle.setObjectName("wdg_detalle")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.wdg_detalle)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.fra_d_superior = QtWidgets.QFrame(self.wdg_detalle)
        self.fra_d_superior.setStyleSheet("background-color: rgb(77, 44, 128);")
        self.fra_d_superior.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_d_superior.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_d_superior.setObjectName("fra_d_superior")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.fra_d_superior)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.fra_table = QtWidgets.QFrame(self.fra_d_superior)
        self.fra_table.setStyleSheet("")
        self.fra_table.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_table.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_table.setObjectName("fra_table")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.fra_table)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.tbl_productos = QtWidgets.QTableWidget(self.fra_table)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tbl_productos.sizePolicy().hasHeightForWidth()
        )
        self.tbl_productos.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.tbl_productos.setFont(font)
        self.tbl_productos.setStyleSheet(
            "QTableWidget {\n"
            "    color: rgb(255,255,255);\n"
            "    background-color: rgb(53, 28, 103);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QHeaderView {\n"
            "    background-color: rgb(53, 28, 103);\n"
            "}\n"
            "\n"
            "QHeaderView::section {\n"
            "    color: rgb(255,255,255);\n"
            "    background-color: rgb(36, 16, 85);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    background-color: rgb(36, 16, 85);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QTableWidget::item {\n"
            "    background-color: rgb(53, 28, 103);\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected {\n"
            "     background-color: rgb(103, 64, 153);\n"
            "}"
        )
        self.tbl_productos.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.tbl_productos.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tbl_productos.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.SingleSelection
        )
        self.tbl_productos.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.tbl_productos.setObjectName("tbl_productos")
        self.tbl_productos.setColumnCount(0)
        self.tbl_productos.setRowCount(0)
        self.verticalLayout_13.addWidget(self.tbl_productos)
        self.verticalLayout_8.addWidget(self.fra_table)
        self.fra_total = QtWidgets.QFrame(self.fra_d_superior)
        self.fra_total.setMaximumSize(QtCore.QSize(16777215, 30))
        self.fra_total.setStyleSheet("background-color: rgb(53, 28, 103);")
        self.fra_total.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_total.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_total.setObjectName("fra_total")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fra_total)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fra_label = QtWidgets.QFrame(self.fra_total)
        self.fra_label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_label.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_label.setObjectName("fra_label")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.fra_label)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.lbl_total = QtWidgets.QLabel(self.fra_label)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.lbl_total.setFont(font)
        self.lbl_total.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.lbl_total.setObjectName("lbl_total")
        self.verticalLayout_12.addWidget(self.lbl_total)
        self.horizontalLayout.addWidget(self.fra_label)
        self.fra_texto = QtWidgets.QFrame(self.fra_total)
        self.fra_texto.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_texto.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_texto.setObjectName("fra_texto")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.fra_texto)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.txt_total = QtWidgets.QLineEdit(self.fra_texto)
        self.txt_total.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_total.sizePolicy().hasHeightForWidth())
        self.txt_total.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.txt_total.setFont(font)
        self.txt_total.setStyleSheet(
            "color: rgb(255,255,255);\n"
            "background-color: rgb(53, 28, 103);\n"
            "border: 0px solid;"
        )
        self.txt_total.setObjectName("txt_total")
        self.verticalLayout_10.addWidget(self.txt_total)
        self.horizontalLayout.addWidget(self.fra_texto)
        self.verticalLayout_8.addWidget(self.fra_total)
        self.verticalLayout_11.addWidget(self.fra_d_superior)
        self.fra_d_inferior = QtWidgets.QFrame(self.wdg_detalle)
        self.fra_d_inferior.setMaximumSize(QtCore.QSize(16777215, 30))
        self.fra_d_inferior.setStyleSheet("background-color: rgb(77, 44, 128);")
        self.fra_d_inferior.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_d_inferior.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_d_inferior.setObjectName("fra_d_inferior")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.fra_d_inferior)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.fra_d_opciones = QtWidgets.QFrame(self.fra_d_inferior)
        self.fra_d_opciones.setStyleSheet("background-color: rgb(77, 44, 128);")
        self.fra_d_opciones.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_d_opciones.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_d_opciones.setObjectName("fra_d_opciones")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.fra_d_opciones)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_finalizar = QtWidgets.QPushButton(self.fra_d_opciones)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_finalizar.sizePolicy().hasHeightForWidth()
        )
        self.btn_finalizar.setSizePolicy(sizePolicy)
        self.btn_finalizar.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.btn_finalizar.setFont(font)
        self.btn_finalizar.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255,255,255);\n"
            "    background-color: rgb(53, 28, 103);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(103, 64, 153);\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "    background-color: rgb(103, 64, 153);\n"
            "    color: rgb(53, 28, 103);\n"
            "}"
        )
        self.btn_finalizar.setObjectName("btn_finalizar")
        self.horizontalLayout_4.addWidget(self.btn_finalizar)
        self.btn_agregar = QtWidgets.QPushButton(self.fra_d_opciones)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_agregar.sizePolicy().hasHeightForWidth())
        self.btn_agregar.setSizePolicy(sizePolicy)
        self.btn_agregar.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.btn_agregar.setFont(font)
        self.btn_agregar.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255,255,255);\n"
            "    background-color: rgb(53, 28, 103);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(103, 64, 153);\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "    background-color: rgb(103, 64, 153);\n"
            "    color: rgb(53, 28, 103);\n"
            "}"
        )
        self.btn_agregar.setObjectName("btn_agregar")
        self.horizontalLayout_4.addWidget(self.btn_agregar)
        self.btn_eliminar = QtWidgets.QPushButton(self.fra_d_opciones)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_eliminar.sizePolicy().hasHeightForWidth())
        self.btn_eliminar.setSizePolicy(sizePolicy)
        self.btn_eliminar.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.btn_eliminar.setFont(font)
        self.btn_eliminar.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255,255,255);\n"
            "    background-color: rgb(53, 28, 103);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(103, 64, 153);\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "    background-color: rgb(103, 64, 153);\n"
            "    color: rgb(53, 28, 103);\n"
            "}"
        )
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.horizontalLayout_4.addWidget(self.btn_eliminar)
        self.btn_d_cancelar = QtWidgets.QPushButton(self.fra_d_opciones)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_d_cancelar.sizePolicy().hasHeightForWidth()
        )
        self.btn_d_cancelar.setSizePolicy(sizePolicy)
        self.btn_d_cancelar.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.btn_d_cancelar.setFont(font)
        self.btn_d_cancelar.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255,255,255);\n"
            "    background-color: rgb(53, 28, 103);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(103, 64, 153);\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "    background-color: rgb(103, 64, 153);\n"
            "    color: rgb(53, 28, 103);\n"
            "}"
        )
        self.btn_d_cancelar.setObjectName("btn_d_cancelar")
        self.horizontalLayout_4.addWidget(self.btn_d_cancelar)
        self.verticalLayout_6.addWidget(
            self.fra_d_opciones, 0, QtCore.Qt.AlignmentFlag.AlignRight
        )
        self.verticalLayout_11.addWidget(self.fra_d_inferior)
        self.stk_factura.addWidget(self.wdg_detalle)
        self.verticalLayout_4.addWidget(self.stk_factura)
        self.verticalLayout.addWidget(self.fra_contenido)

        self.retranslateUi(frm_negocio)
        QtCore.QMetaObject.connectSlotsByName(frm_negocio)

    def retranslateUi(self, frm_negocio):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_titulo.setText(_translate("frm_negocio", "Datos de la factura"))
        self.lbl_cedula.setText(_translate("frm_negocio", "Cédula"))
        self.lbl_nombre.setText(_translate("frm_negocio", "Nombre:"))
        self.lbl_direccion.setText(_translate("frm_negocio", "Dirección:"))
        self.lbl_telefono.setText(_translate("frm_negocio", "Teléfono:"))
        self.lbl_correo.setText(_translate("frm_negocio", "Correo:"))
        self.lbl_m_pago.setText(_translate("frm_negocio", "Método de pago:"))
        self.lbl_fecha.setText(_translate("frm_negocio", "Fecha:"))
        self.btn_continuar.setText(_translate("frm_negocio", "Continuar"))
        self.btn_c_cancelar.setText(_translate("frm_negocio", "Cancelar"))
        self.lbl_total.setText(_translate("frm_negocio", "Total"))
        self.btn_finalizar.setText(_translate("frm_negocio", "Finalizar"))
        self.btn_agregar.setText(_translate("frm_negocio", "Agregar libro"))
        self.btn_eliminar.setText(_translate("frm_negocio", "Eliminar libro"))
        self.btn_d_cancelar.setText(_translate("frm_negocio", "Cancelar"))


class VentanaNegocio(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_frm_negocio()
        self.ui.setupUi(self)
        self.ui.tbl_productos.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Stretch
        )
        self.ui.tbl_productos.verticalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Fixed
        )
        self.ui.tbl_productos.installEventFilter(self)
        self.ui.tbl_productos.viewport().installEventFilter(self)

        self.show()

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.Type.MouseButtonPress:
            if not self.ui.tbl_productos.indexAt(event.pos()).isValid():
                self.ui.tbl_productos.selectionModel().clear()
                self.ui.btn_eliminar.setEnabled(False)
            else:
                self.ui.btn_eliminar.setEnabled(True)
        return super().eventFilter(source, event)
