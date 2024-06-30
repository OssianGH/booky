from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_frm_alterar_usuario(object):
    def setupUi(self, frm_alterar_usuario):
        frm_alterar_usuario.setObjectName("frm_alterar_usuario")
        frm_alterar_usuario.resize(1366, 768)
        frm_alterar_usuario.setWindowTitle("")
        frm_alterar_usuario.setStyleSheet(
            "color: rgb(255,255,255);\n" "background-color: rgb(77, 44, 128);"
        )
        self.verticalLayout = QtWidgets.QVBoxLayout(frm_alterar_usuario)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fra_superior = QtWidgets.QFrame(frm_alterar_usuario)
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
        self.lbl_cedula = QtWidgets.QLabel(self.fra_labels)
        self.lbl_cedula.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.lbl_cedula.setFont(font)
        self.lbl_cedula.setStyleSheet("color: rgb(255,255,255);")
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
        self.txt_cedula = QtWidgets.QLineEdit(self.fra_lines)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_cedula.sizePolicy().hasHeightForWidth())
        self.txt_cedula.setSizePolicy(sizePolicy)
        self.txt_cedula.setMinimumSize(QtCore.QSize(0, 0))
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
        self.txt_cedula.setObjectName("txt_cedula")
        self.verticalLayout_4.addWidget(self.txt_cedula)
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
        self.txt_nombre.setObjectName("txt_nombre")
        self.verticalLayout_4.addWidget(self.txt_nombre)
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
        self.txt_direccion.setObjectName("txt_direccion")
        self.verticalLayout_4.addWidget(self.txt_direccion)
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
        self.txt_telefono.setObjectName("txt_telefono")
        self.verticalLayout_4.addWidget(self.txt_telefono)
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
        self.txt_correo.setObjectName("txt_correo")
        self.verticalLayout_4.addWidget(self.txt_correo)
        self.horizontalLayout.addWidget(self.fra_lines)
        self.verticalLayout.addWidget(self.fra_superior)
        self.fra_inferior = QtWidgets.QFrame(frm_alterar_usuario)
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

        self.retranslateUi(frm_alterar_usuario)
        QtCore.QMetaObject.connectSlotsByName(frm_alterar_usuario)

    def retranslateUi(self, frm_alterar_usuario):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_cedula.setText(_translate("frm_alterar_usuario", "Cédula:"))
        self.lbl_nombre.setText(_translate("frm_alterar_usuario", "Nombre:"))
        self.lbl_direccion.setText(_translate("frm_alterar_usuario", "Dirección:"))
        self.lbl_telefono.setText(_translate("frm_alterar_usuario", "Teléfono:"))
        self.lbl_correo.setText(_translate("frm_alterar_usuario", "Correo:"))
        self.btn_aceptar.setText(_translate("frm_alterar_usuario", "Aceptar"))
        self.btn_cancelar.setText(_translate("frm_alterar_usuario", "Cancelar"))


class VentanaAlterarUsuario(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_frm_alterar_usuario()
        self.ui.setupUi(self)
        self.show()
