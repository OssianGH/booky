from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_frm_portada(object):
    def setupUi(self, frm_portada):
        frm_portada.setObjectName("frm_portada")
        frm_portada.resize(1366, 768)
        frm_portada.setWindowTitle("")
        frm_portada.setStyleSheet(
            "color: rgb(255,255,255);\n" "background-color: rgb(77, 44, 128);"
        )
        self.verticalLayout = QtWidgets.QVBoxLayout(frm_portada)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fra_superior = QtWidgets.QFrame(frm_portada)
        self.fra_superior.setMaximumSize(QtCore.QSize(16777215, 40))
        self.fra_superior.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_superior.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_superior.setObjectName("fra_superior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fra_superior)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fra_caja = QtWidgets.QFrame(self.fra_superior)
        self.fra_caja.setMaximumSize(QtCore.QSize(50, 16777215))
        self.fra_caja.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_caja.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_caja.setObjectName("fra_caja")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.fra_caja)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbl_caja = QtWidgets.QLabel(self.fra_caja)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(14)
        self.lbl_caja.setFont(font)
        self.lbl_caja.setStyleSheet("color: rgb(255,255,255);")
        self.lbl_caja.setObjectName("lbl_caja")
        self.verticalLayout_4.addWidget(self.lbl_caja)
        self.horizontalLayout.addWidget(self.fra_caja)
        self.fra_caja_valor = QtWidgets.QFrame(self.fra_superior)
        self.fra_caja_valor.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_caja_valor.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_caja_valor.setObjectName("fra_caja_valor")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fra_caja_valor)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lbl_caja_valor = QtWidgets.QLabel(self.fra_caja_valor)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.lbl_caja_valor.setFont(font)
        self.lbl_caja_valor.setStyleSheet("color: rgb(255,255,255);")
        self.lbl_caja_valor.setObjectName("lbl_caja_valor")
        self.verticalLayout_5.addWidget(self.lbl_caja_valor)
        self.horizontalLayout.addWidget(self.fra_caja_valor)
        self.verticalLayout.addWidget(self.fra_superior)
        self.fra_central = QtWidgets.QFrame(frm_portada)
        self.fra_central.setStyleSheet("background-color: rgb(53, 28, 103);")
        self.fra_central.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_central.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_central.setObjectName("fra_central")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fra_central)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_logo = QtWidgets.QLabel(self.fra_central)
        self.lbl_logo.setText("")
        self.lbl_logo.setPixmap(QtGui.QPixmap("./resources/logo.png"))
        self.lbl_logo.setScaledContents(False)
        self.lbl_logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_logo.setObjectName("lbl_logo")
        self.verticalLayout_3.addWidget(self.lbl_logo)
        self.lbl_iso = QtWidgets.QLabel(self.fra_central)
        self.lbl_iso.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(14)
        self.lbl_iso.setFont(font)
        self.lbl_iso.setStyleSheet("color: rgb(255,255,255);")
        self.lbl_iso.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.lbl_iso.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_iso.setObjectName("lbl_iso")
        self.verticalLayout_3.addWidget(self.lbl_iso)
        self.verticalLayout.addWidget(self.fra_central)
        self.fra_inferior = QtWidgets.QFrame(frm_portada)
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
        self.btn_vender = QtWidgets.QPushButton(self.fra_opciones)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_vender.sizePolicy().hasHeightForWidth())
        self.btn_vender.setSizePolicy(sizePolicy)
        self.btn_vender.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.btn_vender.setFont(font)
        self.btn_vender.setStyleSheet(
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
        self.btn_vender.setObjectName("btn_vender")
        self.horizontalLayout_2.addWidget(self.btn_vender)
        self.btn_abastecer = QtWidgets.QPushButton(self.fra_opciones)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_abastecer.sizePolicy().hasHeightForWidth()
        )
        self.btn_abastecer.setSizePolicy(sizePolicy)
        self.btn_abastecer.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.btn_abastecer.setFont(font)
        self.btn_abastecer.setStyleSheet(
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
        self.btn_abastecer.setObjectName("btn_abastecer")
        self.horizontalLayout_2.addWidget(self.btn_abastecer)
        self.verticalLayout_2.addWidget(
            self.fra_opciones, 0, QtCore.Qt.AlignmentFlag.AlignRight
        )
        self.verticalLayout.addWidget(self.fra_inferior)

        self.retranslateUi(frm_portada)
        QtCore.QMetaObject.connectSlotsByName(frm_portada)

    def retranslateUi(self, frm_portada):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_caja.setText(_translate("frm_portada", "Caja"))
        self.lbl_iso.setText(_translate("frm_portada", "BOOKY"))
        self.btn_vender.setText(_translate("frm_portada", "Vender"))
        self.btn_abastecer.setText(_translate("frm_portada", "Abastecer"))


class VentanaPortada(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_frm_portada()
        self.ui.setupUi(self)
