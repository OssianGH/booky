from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_frm_ver_libro(object):
    def setupUi(self, frm_ver_libro):
        frm_ver_libro.setObjectName("frm_ver_libro")
        frm_ver_libro.resize(575, 230)
        frm_ver_libro.setWindowTitle("")
        frm_ver_libro.setStyleSheet(
            "color: rgb(255,255,255);\n" "background-color: rgb(77, 44, 128);"
        )
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(frm_ver_libro)
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fra_imagen = QtWidgets.QFrame(frm_ver_libro)
        self.fra_imagen.setMinimumSize(QtCore.QSize(160, 0))
        self.fra_imagen.setMaximumSize(QtCore.QSize(160, 210))
        self.fra_imagen.setStyleSheet("background-color: rgb(53, 28, 103);")
        self.fra_imagen.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_imagen.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_imagen.setObjectName("fra_imagen")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fra_imagen)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lbl_imagen = QtWidgets.QLabel(self.fra_imagen)
        self.lbl_imagen.setScaledContents(True)
        self.lbl_imagen.setObjectName("lbl_imagen")
        self.verticalLayout_5.addWidget(self.lbl_imagen)
        self.horizontalLayout_2.addWidget(self.fra_imagen)
        self.fra_superior = QtWidgets.QFrame(frm_ver_libro)
        self.fra_superior.setStyleSheet("background-color: rgb(53, 28, 103);")
        self.fra_superior.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_superior.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_superior.setObjectName("fra_superior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fra_superior)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fra_labels = QtWidgets.QFrame(self.fra_superior)
        self.fra_labels.setMaximumSize(QtCore.QSize(115, 16777215))
        self.fra_labels.setStyleSheet("background-color: rgb(53, 28, 103);")
        self.fra_labels.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_labels.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_labels.setObjectName("fra_labels")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fra_labels)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_isbn = QtWidgets.QLabel(self.fra_labels)
        self.lbl_isbn.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.lbl_isbn.setFont(font)
        self.lbl_isbn.setStyleSheet("color: rgb(255,255,255);")
        self.lbl_isbn.setObjectName("lbl_isbn")
        self.verticalLayout.addWidget(self.lbl_isbn)
        self.lbl_titulo = QtWidgets.QLabel(self.fra_labels)
        self.lbl_titulo.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setStyleSheet("color: rgb(255,255,255);")
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.verticalLayout.addWidget(self.lbl_titulo)
        self.lbl_p_compra = QtWidgets.QLabel(self.fra_labels)
        self.lbl_p_compra.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.lbl_p_compra.setFont(font)
        self.lbl_p_compra.setStyleSheet("color: rgb(255,255,255);")
        self.lbl_p_compra.setObjectName("lbl_p_compra")
        self.verticalLayout.addWidget(self.lbl_p_compra)
        self.lbl_p_venta = QtWidgets.QLabel(self.fra_labels)
        self.lbl_p_venta.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.lbl_p_venta.setFont(font)
        self.lbl_p_venta.setStyleSheet("color: rgb(255,255,255);")
        self.lbl_p_venta.setObjectName("lbl_p_venta")
        self.verticalLayout.addWidget(self.lbl_p_venta)
        self.lbl_cantidad = QtWidgets.QLabel(self.fra_labels)
        self.lbl_cantidad.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.lbl_cantidad.setFont(font)
        self.lbl_cantidad.setStyleSheet("color: rgb(255,255,255);")
        self.lbl_cantidad.setObjectName("lbl_cantidad")
        self.verticalLayout.addWidget(self.lbl_cantidad)
        self.horizontalLayout.addWidget(self.fra_labels)
        self.fra_lines = QtWidgets.QFrame(self.fra_superior)
        self.fra_lines.setStyleSheet("background-color: rgb(53, 28, 103);")
        self.fra_lines.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_lines.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_lines.setObjectName("fra_lines")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fra_lines)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txt_isbn = QtWidgets.QLineEdit(self.fra_lines)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_isbn.sizePolicy().hasHeightForWidth())
        self.txt_isbn.setSizePolicy(sizePolicy)
        self.txt_isbn.setMinimumSize(QtCore.QSize(250, 0))
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
        self.txt_isbn.setReadOnly(True)
        self.txt_isbn.setObjectName("txt_isbn")
        self.verticalLayout_2.addWidget(self.txt_isbn)
        self.txt_titulo = QtWidgets.QLineEdit(self.fra_lines)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_titulo.sizePolicy().hasHeightForWidth())
        self.txt_titulo.setSizePolicy(sizePolicy)
        self.txt_titulo.setMinimumSize(QtCore.QSize(250, 0))
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
        self.txt_titulo.setReadOnly(True)
        self.txt_titulo.setObjectName("txt_titulo")
        self.verticalLayout_2.addWidget(self.txt_titulo)
        self.txt_p_compra = QtWidgets.QLineEdit(self.fra_lines)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_p_compra.sizePolicy().hasHeightForWidth())
        self.txt_p_compra.setSizePolicy(sizePolicy)
        self.txt_p_compra.setMinimumSize(QtCore.QSize(250, 0))
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
        self.txt_p_compra.setReadOnly(True)
        self.txt_p_compra.setObjectName("txt_p_compra")
        self.verticalLayout_2.addWidget(self.txt_p_compra)
        self.txt_p_venta = QtWidgets.QLineEdit(self.fra_lines)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_p_venta.sizePolicy().hasHeightForWidth())
        self.txt_p_venta.setSizePolicy(sizePolicy)
        self.txt_p_venta.setMinimumSize(QtCore.QSize(250, 0))
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
        self.txt_p_venta.setReadOnly(True)
        self.txt_p_venta.setObjectName("txt_p_venta")
        self.verticalLayout_2.addWidget(self.txt_p_venta)
        self.txt_cantidad = QtWidgets.QLineEdit(self.fra_lines)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_cantidad.sizePolicy().hasHeightForWidth())
        self.txt_cantidad.setSizePolicy(sizePolicy)
        self.txt_cantidad.setMinimumSize(QtCore.QSize(250, 0))
        self.txt_cantidad.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.txt_cantidad.setFont(font)
        self.txt_cantidad.setStyleSheet(
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
        self.txt_cantidad.setReadOnly(True)
        self.txt_cantidad.setObjectName("txt_cantidad")
        self.verticalLayout_2.addWidget(self.txt_cantidad)
        self.horizontalLayout.addWidget(self.fra_lines)
        self.horizontalLayout_2.addWidget(self.fra_superior)

        self.retranslateUi(frm_ver_libro)
        QtCore.QMetaObject.connectSlotsByName(frm_ver_libro)

    def retranslateUi(self, frm_ver_libro):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_isbn.setText(_translate("frm_ver_libro", "ISBN:"))
        self.lbl_titulo.setText(_translate("frm_ver_libro", "Título:"))
        self.lbl_p_compra.setText(_translate("frm_ver_libro", "Precio compra:"))
        self.lbl_p_venta.setText(_translate("frm_ver_libro", "Precio venta:"))
        self.lbl_cantidad.setText(_translate("frm_ver_libro", "Cantidad:"))


class VentanaVerLibro(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_frm_ver_libro()
        self.ui.setupUi(self)
        self.show()
