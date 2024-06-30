from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_frm_alterar_libro(object):
    def setupUi(self, frm_alterar_libro):
        frm_alterar_libro.setObjectName("frm_alterar_libro")
        frm_alterar_libro.resize(1366, 768)
        frm_alterar_libro.setWindowTitle("")
        frm_alterar_libro.setStyleSheet(
            "color: rgb(255,255,255);\n" "background-color: rgb(77, 44, 128);"
        )
        self.verticalLayout = QtWidgets.QVBoxLayout(frm_alterar_libro)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fra_superior = QtWidgets.QFrame(frm_alterar_libro)
        self.fra_superior.setStyleSheet("background-color: rgb(53, 28, 103);")
        self.fra_superior.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_superior.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_superior.setObjectName("fra_superior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fra_superior)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fra_labels = QtWidgets.QFrame(self.fra_superior)
        self.fra_labels.setMaximumSize(QtCore.QSize(150, 16777215))
        self.fra_labels.setStyleSheet("background-color: rgb(53, 28, 103);")
        self.fra_labels.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_labels.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_labels.setObjectName("fra_labels")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fra_labels)
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_isbn = QtWidgets.QLabel(self.fra_labels)
        self.lbl_isbn.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.lbl_isbn.setFont(font)
        self.lbl_isbn.setStyleSheet("color: rgb(255,255,255);")
        self.lbl_isbn.setObjectName("lbl_isbn")
        self.verticalLayout_3.addWidget(self.lbl_isbn)
        self.lbl_titulo = QtWidgets.QLabel(self.fra_labels)
        self.lbl_titulo.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setStyleSheet("color: rgb(255,255,255);")
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.verticalLayout_3.addWidget(self.lbl_titulo)
        self.lbl_p_compra = QtWidgets.QLabel(self.fra_labels)
        self.lbl_p_compra.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.lbl_p_compra.setFont(font)
        self.lbl_p_compra.setStyleSheet("color: rgb(255,255,255);")
        self.lbl_p_compra.setObjectName("lbl_p_compra")
        self.verticalLayout_3.addWidget(self.lbl_p_compra)
        self.lbl_p_venta = QtWidgets.QLabel(self.fra_labels)
        self.lbl_p_venta.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.lbl_p_venta.setFont(font)
        self.lbl_p_venta.setStyleSheet("color: rgb(255,255,255);")
        self.lbl_p_venta.setObjectName("lbl_p_venta")
        self.verticalLayout_3.addWidget(self.lbl_p_venta)
        self.lbl_portada = QtWidgets.QLabel(self.fra_labels)
        self.lbl_portada.setMinimumSize(QtCore.QSize(0, 230))
        self.lbl_portada.setMaximumSize(QtCore.QSize(16777215, 230))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.lbl_portada.setFont(font)
        self.lbl_portada.setStyleSheet("color: rgb(255,255,255);")
        self.lbl_portada.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lbl_portada.setObjectName("lbl_portada")
        self.verticalLayout_3.addWidget(self.lbl_portada)
        self.horizontalLayout.addWidget(self.fra_labels)
        self.fra_lines = QtWidgets.QFrame(self.fra_superior)
        self.fra_lines.setStyleSheet("background-color: rgb(53, 28, 103);")
        self.fra_lines.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_lines.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_lines.setObjectName("fra_lines")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.fra_lines)
        self.verticalLayout_4.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_4.setSpacing(30)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.txt_isbn = QtWidgets.QLineEdit(self.fra_lines)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_isbn.sizePolicy().hasHeightForWidth())
        self.txt_isbn.setSizePolicy(sizePolicy)
        self.txt_isbn.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.txt_isbn.setFont(font)
        self.txt_isbn.setStyleSheet(
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
        self.txt_isbn.setObjectName("txt_isbn")
        self.verticalLayout_4.addWidget(self.txt_isbn)
        self.txt_titulo = QtWidgets.QLineEdit(self.fra_lines)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_titulo.sizePolicy().hasHeightForWidth())
        self.txt_titulo.setSizePolicy(sizePolicy)
        self.txt_titulo.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.txt_titulo.setFont(font)
        self.txt_titulo.setStyleSheet(
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
        self.txt_titulo.setObjectName("txt_titulo")
        self.verticalLayout_4.addWidget(self.txt_titulo)
        self.txt_p_compra = QtWidgets.QLineEdit(self.fra_lines)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_p_compra.sizePolicy().hasHeightForWidth())
        self.txt_p_compra.setSizePolicy(sizePolicy)
        self.txt_p_compra.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.txt_p_compra.setFont(font)
        self.txt_p_compra.setStyleSheet(
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
        self.txt_p_compra.setObjectName("txt_p_compra")
        self.verticalLayout_4.addWidget(self.txt_p_compra)
        self.txt_p_venta = QtWidgets.QLineEdit(self.fra_lines)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_p_venta.sizePolicy().hasHeightForWidth())
        self.txt_p_venta.setSizePolicy(sizePolicy)
        self.txt_p_venta.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.txt_p_venta.setFont(font)
        self.txt_p_venta.setStyleSheet(
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
        self.txt_p_venta.setObjectName("txt_p_venta")
        self.verticalLayout_4.addWidget(self.txt_p_venta)
        self.fra_input_imagen = QtWidgets.QFrame(self.fra_lines)
        self.fra_input_imagen.setMinimumSize(QtCore.QSize(160, 0))
        self.fra_input_imagen.setMaximumSize(QtCore.QSize(160, 230))
        self.fra_input_imagen.setStyleSheet("background-color: rgb(53, 28, 103);")
        self.fra_input_imagen.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_input_imagen.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_input_imagen.setObjectName("fra_input_imagen")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fra_input_imagen)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.fra_boton = QtWidgets.QFrame(self.fra_input_imagen)
        self.fra_boton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.fra_boton.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_boton.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_boton.setObjectName("fra_boton")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.fra_boton)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btn_imagen = QtWidgets.QPushButton(self.fra_boton)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_imagen.sizePolicy().hasHeightForWidth())
        self.btn_imagen.setSizePolicy(sizePolicy)
        self.btn_imagen.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.btn_imagen.setFont(font)
        self.btn_imagen.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255,255,255);\n"
            "    background-color: rgb(77, 44, 128);\n"
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
        self.btn_imagen.setObjectName("btn_imagen")
        self.verticalLayout_6.addWidget(
            self.btn_imagen, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.verticalLayout_5.addWidget(self.fra_boton)
        self.fra_imagen = QtWidgets.QFrame(self.fra_input_imagen)
        self.fra_imagen.setStyleSheet("background-color: rgb(77, 44, 128);")
        self.fra_imagen.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_imagen.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_imagen.setObjectName("fra_imagen")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.fra_imagen)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lbl_imagen = QtWidgets.QLabel(self.fra_imagen)
        self.lbl_imagen.setScaledContents(True)
        self.lbl_imagen.setObjectName("lbl_imagen")
        self.verticalLayout_7.addWidget(self.lbl_imagen)
        self.verticalLayout_5.addWidget(self.fra_imagen)
        self.verticalLayout_4.addWidget(
            self.fra_input_imagen, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.horizontalLayout.addWidget(self.fra_lines)
        self.verticalLayout.addWidget(self.fra_superior)
        self.fra_inferior = QtWidgets.QFrame(frm_alterar_libro)
        self.fra_inferior.setMaximumSize(QtCore.QSize(16777215, 30))
        self.fra_inferior.setStyleSheet("background-color: rgb(77, 44, 128);")
        self.fra_inferior.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_inferior.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_inferior.setObjectName("fra_inferior")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fra_inferior)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fra_opciones = QtWidgets.QFrame(self.fra_inferior)
        self.fra_opciones.setStyleSheet("background-color: rgb(77, 44, 128);")
        self.fra_opciones.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_opciones.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_opciones.setObjectName("fra_opciones")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fra_opciones)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_aceptar = QtWidgets.QPushButton(self.fra_opciones)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_aceptar.sizePolicy().hasHeightForWidth())
        self.btn_aceptar.setSizePolicy(sizePolicy)
        self.btn_aceptar.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.btn_aceptar.setFont(font)
        self.btn_aceptar.setStyleSheet(
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
        self.btn_aceptar.setObjectName("btn_aceptar")
        self.horizontalLayout_2.addWidget(self.btn_aceptar)
        self.btn_cancelar = QtWidgets.QPushButton(self.fra_opciones)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancelar.sizePolicy().hasHeightForWidth())
        self.btn_cancelar.setSizePolicy(sizePolicy)
        self.btn_cancelar.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.btn_cancelar.setFont(font)
        self.btn_cancelar.setStyleSheet(
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
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.horizontalLayout_2.addWidget(self.btn_cancelar)
        self.verticalLayout_2.addWidget(
            self.fra_opciones, 0, QtCore.Qt.AlignmentFlag.AlignRight
        )
        self.verticalLayout.addWidget(self.fra_inferior)

        self.retranslateUi(frm_alterar_libro)
        QtCore.QMetaObject.connectSlotsByName(frm_alterar_libro)

    def retranslateUi(self, frm_alterar_libro):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_isbn.setText(_translate("frm_alterar_libro", "ISBN:"))
        self.lbl_titulo.setText(_translate("frm_alterar_libro", "Título:"))
        self.lbl_p_compra.setText(_translate("frm_alterar_libro", "Precio compra:"))
        self.lbl_p_venta.setText(_translate("frm_alterar_libro", "Precio venta:"))
        self.lbl_portada.setText(_translate("frm_alterar_libro", "Portada:"))
        self.btn_imagen.setText(_translate("frm_alterar_libro", "Cargar imagen"))
        self.btn_aceptar.setText(_translate("frm_alterar_libro", "Aceptar"))
        self.btn_cancelar.setText(_translate("frm_alterar_libro", "Cancelar"))


class VentanaAlterarLibro(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_frm_alterar_libro()
        self.ui.setupUi(self)
        self.show()
