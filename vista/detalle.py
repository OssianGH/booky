from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_frm_detalle(object):
    def setupUi(self, frm_detalle):
        frm_detalle.setObjectName("frm_detalle")
        frm_detalle.resize(1366, 768)
        frm_detalle.setStyleSheet(
            "color: rgb(255,255,255);\n" "background-color: rgb(77, 44, 128);"
        )
        self.verticalLayout = QtWidgets.QVBoxLayout(frm_detalle)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fra_detalle = QtWidgets.QFrame(frm_detalle)
        self.fra_detalle.setStyleSheet("background-color: rgb(53, 28, 103);")
        self.fra_detalle.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_detalle.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_detalle.setObjectName("fra_detalle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fra_detalle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tbl_detalle = QtWidgets.QTableWidget(self.fra_detalle)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_detalle.sizePolicy().hasHeightForWidth())
        self.tbl_detalle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.tbl_detalle.setFont(font)
        self.tbl_detalle.setStyleSheet(
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
        self.tbl_detalle.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.tbl_detalle.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tbl_detalle.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.SingleSelection
        )
        self.tbl_detalle.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.tbl_detalle.setObjectName("tbl_detalle")
        self.tbl_detalle.setColumnCount(0)
        self.tbl_detalle.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tbl_detalle)
        self.verticalLayout.addWidget(self.fra_detalle)
        self.fra_inferior = QtWidgets.QFrame(frm_detalle)
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

        self.retranslateUi(frm_detalle)
        QtCore.QMetaObject.connectSlotsByName(frm_detalle)

    def retranslateUi(self, frm_detalle):
        _translate = QtCore.QCoreApplication.translate
        frm_detalle.setWindowTitle(_translate("frm_detalle", "Detalle de la factura"))
        self.btn_cerrar.setText(_translate("frm_detalle", "Cerrar"))


class VentanaDetalle(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_frm_detalle()
        self.ui.setupUi(self)
        self.ui.tbl_detalle.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Stretch
        )
        self.ui.tbl_detalle.verticalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Fixed
        )
        self.show()
