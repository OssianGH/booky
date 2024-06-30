from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_frm_select_libro(object):
    def setupUi(self, frm_select_libro):
        frm_select_libro.setObjectName("frm_select_libro")
        frm_select_libro.resize(1024, 576)
        frm_select_libro.setStyleSheet(
            "color: rgb(255,255,255);\n" "background-color: rgb(77, 44, 128);"
        )
        self.verticalLayout = QtWidgets.QVBoxLayout(frm_select_libro)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(frm_select_libro)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fra_label = QtWidgets.QFrame(self.frame)
        self.fra_label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.fra_label.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fra_label.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
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
        self.fra_texto.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fra_texto.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fra_texto.setObjectName("fra_texto")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fra_texto)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.txt_isbn = QtWidgets.QLineEdit(self.fra_texto)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_isbn.sizePolicy().hasHeightForWidth())
        self.txt_isbn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.txt_isbn.setFont(font)
        self.txt_isbn.setStyleSheet(
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
        self.txt_isbn.setObjectName("txt_isbn")
        self.verticalLayout_3.addWidget(self.txt_isbn)
        self.horizontalLayout_3.addWidget(self.fra_texto)
        self.verticalLayout.addWidget(self.frame)
        self.fra_libros = QtWidgets.QFrame(frm_select_libro)
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
        self.fra_inferior = QtWidgets.QFrame(frm_select_libro)
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

        self.retranslateUi(frm_select_libro)
        QtCore.QMetaObject.connectSlotsByName(frm_select_libro)

    def retranslateUi(self, frm_select_libro):
        _translate = QtCore.QCoreApplication.translate
        frm_select_libro.setWindowTitle(
            _translate("frm_select_libro", "Agregar libro a la factura")
        )
        self.lbl_isbn.setText(_translate("frm_select_libro", "ISBN:"))
        self.btn_cerrar.setText(_translate("frm_select_libro", "Cerrar"))


class VentanaSelectLibro(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_frm_select_libro()
        self.ui.setupUi(self)
        self.ui.tbl_libros.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Stretch
        )
        self.ui.tbl_libros.verticalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Fixed
        )
        self.ui.tbl_libros.installEventFilter(self)
        self.ui.tbl_libros.viewport().installEventFilter(self)
        self.show()

    def eventFilter(self, source, event):
        if (
            event.type() == QtCore.QEvent.Type.MouseButtonDblClick
            and event.buttons() == QtCore.Qt.MouseButton.LeftButton
            and self.ui.tbl_libros.itemAt(event.pos()) is not None
        ):
            self.close()
        if event.type() == QtCore.QEvent.Type.MouseButtonPress:
            if not self.ui.tbl_libros.indexAt(event.pos()).isValid():
                self.ui.tbl_libros.selectionModel().clear()
        return super().eventFilter(source, event)
