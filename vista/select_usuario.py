from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_frm_select_usuario(object):
    def setupUi(self, frm_select_usuario):
        frm_select_usuario.setObjectName("frm_select_usuario")
        frm_select_usuario.resize(1024, 576)
        frm_select_usuario.setStyleSheet(
            "color: rgb(255,255,255);\n" "background-color: rgb(77, 44, 128);"
        )
        self.verticalLayout = QtWidgets.QVBoxLayout(frm_select_usuario)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(frm_select_usuario)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fra_label = QtWidgets.QFrame(self.frame)
        self.fra_label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.fra_label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_label.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_label.setObjectName("fra_label")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.fra_label)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbl_isbn = QtWidgets.QLabel(self.fra_label)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.lbl_isbn.setFont(font)
        self.lbl_isbn.setStyleSheet("color: rgb(255,255,255);")
        self.lbl_isbn.setObjectName("lbl_isbn")
        self.verticalLayout_4.addWidget(self.lbl_isbn)
        self.horizontalLayout_3.addWidget(self.fra_label)
        self.fra_texto = QtWidgets.QFrame(self.frame)
        self.fra_texto.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_texto.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_texto.setObjectName("fra_texto")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fra_texto)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.txt_cedula = QtWidgets.QLineEdit(self.fra_texto)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_cedula.sizePolicy().hasHeightForWidth())
        self.txt_cedula.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.txt_cedula.setFont(font)
        self.txt_cedula.setStyleSheet(
            "QLineEdit {\n"
            "    color: rgb(255,255,255);\n"
            "    background-color: rgb(53, 28, 103);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QLineEdit:disabled {\n"
            "    color: rgb(53, 28, 103);\n"
            "    background-color: rgb(103, 64, 153);\n"
            "}"
        )
        self.txt_cedula.setObjectName("txt_cedula")
        self.verticalLayout_3.addWidget(self.txt_cedula)
        self.horizontalLayout_3.addWidget(self.fra_texto)
        self.verticalLayout.addWidget(self.frame)
        self.fra_usuarios = QtWidgets.QFrame(frm_select_usuario)
        self.fra_usuarios.setStyleSheet("background-color: rgb(53, 28, 103);")
        self.fra_usuarios.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_usuarios.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_usuarios.setObjectName("fra_usuarios")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fra_usuarios)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tbl_usuarios = QtWidgets.QTableWidget(self.fra_usuarios)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_usuarios.sizePolicy().hasHeightForWidth())
        self.tbl_usuarios.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.tbl_usuarios.setFont(font)
        self.tbl_usuarios.setStyleSheet(
            "QTableWidget {\n"
            "    color: rgb(255,255,255);\n"
            "    background-color: rgb(53, 28, 103);\n"
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
        self.tbl_usuarios.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.tbl_usuarios.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tbl_usuarios.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.SingleSelection
        )
        self.tbl_usuarios.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.tbl_usuarios.setObjectName("tbl_usuarios")
        self.tbl_usuarios.setColumnCount(0)
        self.tbl_usuarios.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tbl_usuarios)
        self.verticalLayout.addWidget(self.fra_usuarios)
        self.fra_inferior = QtWidgets.QFrame(frm_select_usuario)
        self.fra_inferior.setMaximumSize(QtCore.QSize(16777215, 30))
        self.fra_inferior.setStyleSheet("background-color: rgb(77, 44, 128);")
        self.fra_inferior.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_inferior.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_inferior.setObjectName("fra_inferior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fra_inferior)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fra_opciones = QtWidgets.QFrame(self.fra_inferior)
        self.fra_opciones.setStyleSheet("background-color: rgb(77, 44, 128);")
        self.fra_opciones.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_opciones.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_opciones.setObjectName("fra_opciones")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fra_opciones)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_cerrar = QtWidgets.QPushButton(self.fra_opciones)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cerrar.sizePolicy().hasHeightForWidth())
        self.btn_cerrar.setSizePolicy(sizePolicy)
        self.btn_cerrar.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.btn_cerrar.setFont(font)
        self.btn_cerrar.setStyleSheet(
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
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.horizontalLayout_2.addWidget(self.btn_cerrar)
        self.horizontalLayout.addWidget(
            self.fra_opciones, 0, QtCore.Qt.AlignmentFlag.AlignRight
        )
        self.verticalLayout.addWidget(self.fra_inferior)

        self.retranslateUi(frm_select_usuario)
        QtCore.QMetaObject.connectSlotsByName(frm_select_usuario)

    def retranslateUi(self, frm_select_usuario):
        _translate = QtCore.QCoreApplication.translate
        frm_select_usuario.setWindowTitle(
            _translate(
                "frm_select_usuario",
                "Seleccionar cliente o proveedor para los datos de la factura",
            )
        )
        self.lbl_isbn.setText(_translate("frm_select_usuario", "Cédula:"))
        self.btn_cerrar.setText(_translate("frm_select_usuario", "Cerrar"))


class VentanaSelectUsuario(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_frm_select_usuario()
        self.ui.setupUi(self)
        self.ui.tbl_usuarios.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Stretch
        )
        self.ui.tbl_usuarios.verticalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Fixed
        )
        self.ui.tbl_usuarios.installEventFilter(self)
        self.ui.tbl_usuarios.viewport().installEventFilter(self)
        self.show()

    def eventFilter(self, source, event):
        if (
            event.type() == QtCore.QEvent.Type.MouseButtonDblClick
            and event.buttons() == QtCore.Qt.MouseButton.LeftButton
            and self.ui.tbl_usuarios.itemAt(event.pos()) is not None
        ):
            self.close()
        if event.type() == QtCore.QEvent.Type.MouseButtonPress:
            if not self.ui.tbl_usuarios.indexAt(event.pos()).isValid():
                self.ui.tbl_usuarios.selectionModel().clear()
        return super().eventFilter(source, event)
