from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_frm_libros(object):
    def setupUi(self, frm_libros):
        frm_libros.setObjectName("frm_libros")
        frm_libros.resize(1366, 768)
        frm_libros.setStyleSheet(
            "color: rgb(255,255,255);\n" "background-color: rgb(77, 44, 128);"
        )
        self.verticalLayout = QtWidgets.QVBoxLayout(frm_libros)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fra_titulo = QtWidgets.QFrame(frm_libros)
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
        self.fra_superior = QtWidgets.QFrame(frm_libros)
        self.fra_superior.setMaximumSize(QtCore.QSize(16777215, 30))
        self.fra_superior.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_superior.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_superior.setObjectName("fra_superior")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.fra_superior)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fra_label = QtWidgets.QFrame(self.fra_superior)
        self.fra_label.setMaximumSize(QtCore.QSize(80, 16777215))
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
        self.fra_combo = QtWidgets.QFrame(self.fra_superior)
        self.fra_combo.setMaximumSize(QtCore.QSize(140, 16777215))
        self.fra_combo.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_combo.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_combo.setObjectName("fra_combo")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fra_combo)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.cmb_criterio = QtWidgets.QComboBox(self.fra_combo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_criterio.sizePolicy().hasHeightForWidth())
        self.cmb_criterio.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.cmb_criterio.setFont(font)
        self.cmb_criterio.setStyleSheet(
            "color: rgb(255,255,255);\n"
            "background-color: rgb(53, 28, 103);\n"
            "border: 0px solid;"
        )
        self.cmb_criterio.setObjectName("cmb_criterio")
        self.verticalLayout_5.addWidget(self.cmb_criterio)
        self.horizontalLayout_3.addWidget(self.fra_combo)
        self.fra_query = QtWidgets.QFrame(self.fra_superior)
        self.fra_query.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_query.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_query.setObjectName("fra_query")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.fra_query)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
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
        self.txt_query.setObjectName("txt_query")
        self.verticalLayout_6.addWidget(self.txt_query)
        self.horizontalLayout_3.addWidget(self.fra_query)
        self.verticalLayout.addWidget(self.fra_superior)
        self.fra_libros = QtWidgets.QFrame(frm_libros)
        self.fra_libros.setStyleSheet("background-color: rgb(53, 28, 103);")
        self.fra_libros.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_libros.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_libros.setObjectName("fra_libros")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fra_libros)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tbl_libros = QtWidgets.QTableWidget(self.fra_libros)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_libros.sizePolicy().hasHeightForWidth())
        self.tbl_libros.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.tbl_libros.setFont(font)
        self.tbl_libros.setStyleSheet(
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
        self.tbl_libros.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.tbl_libros.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tbl_libros.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.SingleSelection
        )
        self.tbl_libros.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.tbl_libros.setObjectName("tbl_libros")
        self.tbl_libros.setColumnCount(0)
        self.tbl_libros.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tbl_libros)
        self.verticalLayout.addWidget(self.fra_libros)
        self.fra_inferior = QtWidgets.QFrame(frm_libros)
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
        self.btn_transacciones = QtWidgets.QPushButton(self.fra_opciones)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_transacciones.sizePolicy().hasHeightForWidth()
        )
        self.btn_transacciones.setSizePolicy(sizePolicy)
        self.btn_transacciones.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.btn_transacciones.setFont(font)
        self.btn_transacciones.setStyleSheet(
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
        self.btn_transacciones.setObjectName("btn_transacciones")
        self.horizontalLayout_2.addWidget(self.btn_transacciones)
        self.horizontalLayout.addWidget(
            self.fra_opciones, 0, QtCore.Qt.AlignmentFlag.AlignRight
        )
        self.verticalLayout.addWidget(self.fra_inferior)

        self.retranslateUi(frm_libros)
        QtCore.QMetaObject.connectSlotsByName(frm_libros)

    def retranslateUi(self, frm_libros):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_titulo.setText(_translate("frm_libros", "Libros"))
        self.lbl_buscar.setText(_translate("frm_libros", "Buscar por:"))
        self.btn_nuevo.setText(_translate("frm_libros", "Nuevo"))
        self.btn_editar.setText(_translate("frm_libros", "Editar"))
        self.btn_eliminar.setText(_translate("frm_libros", "Eliminar"))
        self.btn_transacciones.setText(_translate("frm_libros", "Transacciones"))


class VentanaLibros(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_frm_libros()
        self.ui.setupUi(self)
        self.ui.tbl_libros.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Stretch
        )
        self.ui.tbl_libros.verticalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Fixed
        )
        self.ui.tbl_libros.installEventFilter(self)
        self.ui.tbl_libros.viewport().installEventFilter(self)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.Type.MouseButtonPress:
            if not self.ui.tbl_libros.indexAt(event.pos()).isValid():
                self.ui.tbl_libros.selectionModel().clear()
                self.activar_botones(False)
            else:
                self.activar_botones()
        return super().eventFilter(source, event)

    def activar_botones(self, criterio=True):
        self.ui.btn_editar.setEnabled(criterio)
        self.ui.btn_eliminar.setEnabled(criterio)
        self.ui.btn_transacciones.setEnabled(criterio)
