from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_frm_facturas(object):
    def setupUi(self, frm_facturas):
        frm_facturas.setObjectName("frm_facturas")
        frm_facturas.resize(1366, 768)
        frm_facturas.setStyleSheet(
            "color: rgb(255,255,255);\n" "background-color: rgb(77, 44, 128);"
        )
        self.verticalLayout = QtWidgets.QVBoxLayout(frm_facturas)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fra_titulo = QtWidgets.QFrame(frm_facturas)
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
        self.fra_facturas = QtWidgets.QFrame(frm_facturas)
        self.fra_facturas.setStyleSheet("background-color: rgb(53, 28, 103);")
        self.fra_facturas.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_facturas.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_facturas.setObjectName("fra_facturas")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fra_facturas)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tbl_facturas = QtWidgets.QTableWidget(self.fra_facturas)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_facturas.sizePolicy().hasHeightForWidth())
        self.tbl_facturas.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.tbl_facturas.setFont(font)
        self.tbl_facturas.setStyleSheet(
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
        self.tbl_facturas.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.tbl_facturas.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tbl_facturas.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.SingleSelection
        )
        self.tbl_facturas.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.tbl_facturas.setObjectName("tbl_facturas")
        self.tbl_facturas.setColumnCount(0)
        self.tbl_facturas.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tbl_facturas)
        self.verticalLayout.addWidget(self.fra_facturas)
        self.fra_inferior = QtWidgets.QFrame(frm_facturas)
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
        self.btn_detalle = QtWidgets.QPushButton(self.fra_opciones)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_detalle.sizePolicy().hasHeightForWidth())
        self.btn_detalle.setSizePolicy(sizePolicy)
        self.btn_detalle.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.btn_detalle.setFont(font)
        self.btn_detalle.setStyleSheet(
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
        self.btn_detalle.setObjectName("btn_detalle")
        self.horizontalLayout_2.addWidget(self.btn_detalle)
        self.horizontalLayout.addWidget(
            self.fra_opciones, 0, QtCore.Qt.AlignmentFlag.AlignRight
        )
        self.verticalLayout.addWidget(self.fra_inferior)

        self.retranslateUi(frm_facturas)
        QtCore.QMetaObject.connectSlotsByName(frm_facturas)

    def retranslateUi(self, frm_facturas):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_titulo.setText(_translate("frm_facturas", "Facturas"))
        self.btn_detalle.setText(_translate("frm_facturas", "Detalle"))


class VentanaFacturas(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_frm_facturas()
        self.ui.setupUi(self)
        self.ui.tbl_facturas.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Stretch
        )
        self.ui.tbl_facturas.verticalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Fixed
        )
        self.ui.tbl_facturas.installEventFilter(self)
        self.ui.tbl_facturas.viewport().installEventFilter(self)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.Type.MouseButtonPress:
            if not self.ui.tbl_facturas.indexAt(event.pos()).isValid():
                self.ui.tbl_facturas.selectionModel().clear()
                self.ui.btn_detalle.setEnabled(False)
            else:
                self.ui.btn_detalle.setEnabled(True)
        return super().eventFilter(source, event)
