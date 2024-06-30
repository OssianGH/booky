from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_frm_usuarios(object):
    def setupUi(self, frm_usuarios):
        frm_usuarios.setObjectName("frm_usuarios")
        frm_usuarios.resize(1366, 768)
        frm_usuarios.setStyleSheet(
            "color: rgb(255,255,255);\n" "background-color: rgb(77, 44, 128);"
        )
        self.verticalLayout = QtWidgets.QVBoxLayout(frm_usuarios)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fra_titulo = QtWidgets.QFrame(frm_usuarios)
        self.fra_titulo.setMaximumSize(QtCore.QSize(16777215, 40))
        self.fra_titulo.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_titulo.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_titulo.setObjectName("fra_titulo")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fra_titulo)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_titulo = QtWidgets.QLabel(self.fra_titulo)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(14)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setStyleSheet("color: rgb(255,255,255);")
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.verticalLayout_3.addWidget(self.lbl_titulo)
        self.verticalLayout.addWidget(self.fra_titulo)
        self.fra_superior = QtWidgets.QFrame(frm_usuarios)
        self.fra_superior.setMaximumSize(QtCore.QSize(16777215, 30))
        self.fra_superior.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_superior.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_superior.setObjectName("fra_superior")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.fra_superior)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fra_label = QtWidgets.QFrame(self.fra_superior)
        self.fra_label.setMaximumSize(QtCore.QSize(130, 16777215))
        self.fra_label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_label.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_label.setObjectName("fra_label")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.fra_label)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbl_buscar = QtWidgets.QLabel(self.fra_label)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.lbl_buscar.setFont(font)
        self.lbl_buscar.setStyleSheet("color: rgb(255,255,255);")
        self.lbl_buscar.setObjectName("lbl_buscar")
        self.verticalLayout_4.addWidget(self.lbl_buscar)
        self.horizontalLayout_3.addWidget(self.fra_label)
        self.fra_query = QtWidgets.QFrame(self.fra_superior)
        self.fra_query.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_query.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_query.setObjectName("fra_query")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fra_query)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.txt_query = QtWidgets.QLineEdit(self.fra_query)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_query.sizePolicy().hasHeightForWidth())
        self.txt_query.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.txt_query.setFont(font)
        self.txt_query.setStyleSheet(
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
        self.txt_query.setReadOnly(False)
        self.txt_query.setObjectName("txt_query")
        self.verticalLayout_5.addWidget(self.txt_query)
        self.horizontalLayout_3.addWidget(self.fra_query)
        self.verticalLayout.addWidget(self.fra_superior)
        self.fra_usuarios = QtWidgets.QFrame(frm_usuarios)
        self.fra_usuarios.setStyleSheet("background-color: rgb(77, 44, 128);")
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
        self.fra_inferior = QtWidgets.QFrame(frm_usuarios)
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
        self.btn_nuevo = QtWidgets.QPushButton(self.fra_opciones)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_nuevo.sizePolicy().hasHeightForWidth())
        self.btn_nuevo.setSizePolicy(sizePolicy)
        self.btn_nuevo.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.btn_nuevo.setFont(font)
        self.btn_nuevo.setStyleSheet(
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
        self.btn_nuevo.setObjectName("btn_nuevo")
        self.horizontalLayout_2.addWidget(self.btn_nuevo)
        self.btn_editar = QtWidgets.QPushButton(self.fra_opciones)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_editar.sizePolicy().hasHeightForWidth())
        self.btn_editar.setSizePolicy(sizePolicy)
        self.btn_editar.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.btn_editar.setFont(font)
        self.btn_editar.setStyleSheet(
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
        self.btn_editar.setObjectName("btn_editar")
        self.horizontalLayout_2.addWidget(self.btn_editar)
        self.btn_eliminar = QtWidgets.QPushButton(self.fra_opciones)
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
        self.horizontalLayout_2.addWidget(self.btn_eliminar)
        self.horizontalLayout.addWidget(
            self.fra_opciones, 0, QtCore.Qt.AlignmentFlag.AlignRight
        )
        self.verticalLayout.addWidget(self.fra_inferior)

        self.retranslateUi(frm_usuarios)
        QtCore.QMetaObject.connectSlotsByName(frm_usuarios)

    def retranslateUi(self, frm_usuarios):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_titulo.setText(_translate("frm_usuarios", "Título"))
        self.lbl_buscar.setText(_translate("frm_usuarios", "Buscar por cédula"))
        self.btn_nuevo.setText(_translate("frm_usuarios", "Nuevo"))
        self.btn_editar.setText(_translate("frm_usuarios", "Editar"))
        self.btn_eliminar.setText(_translate("frm_usuarios", "Eliminar"))


class VentanaUsuarios(QtWidgets.QWidget):
    def __init__(self, titulo):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_frm_usuarios()
        self.ui.setupUi(self)
        self.ui.lbl_titulo.setText(titulo)
        self.ui.tbl_usuarios.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Stretch
        )
        self.ui.tbl_usuarios.verticalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Fixed
        )
        self.ui.tbl_usuarios.installEventFilter(self)
        self.ui.tbl_usuarios.viewport().installEventFilter(self)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.Type.MouseButtonPress:
            if not self.ui.tbl_usuarios.indexAt(event.pos()).isValid():
                self.ui.tbl_usuarios.selectionModel().clear()
                self.activar_botones(False)
            else:
                self.activar_botones()
        return super().eventFilter(source, event)

    def activar_botones(self, criterio=True):
        self.ui.btn_editar.setEnabled(criterio)
        self.ui.btn_eliminar.setEnabled(criterio)
