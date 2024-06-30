from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_frm_transacciones(object):
    def setupUi(self, frm_transacciones):
        frm_transacciones.setObjectName("frm_transacciones")
        frm_transacciones.resize(1366, 768)
        frm_transacciones.setStyleSheet(
            "color: rgb(255,255,255);\n" "background-color: rgb(77, 44, 128);"
        )
        self.verticalLayout = QtWidgets.QVBoxLayout(frm_transacciones)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fra_superior = QtWidgets.QFrame(frm_transacciones)
        self.fra_superior.setMaximumSize(QtCore.QSize(16777215, 30))
        self.fra_superior.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_superior.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_superior.setObjectName("fra_superior")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.fra_superior)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cmb_criterio = QtWidgets.QComboBox(self.fra_superior)
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
        self.horizontalLayout_3.addWidget(self.cmb_criterio)
        self.verticalLayout.addWidget(self.fra_superior)
        self.fra_transacciones = QtWidgets.QFrame(frm_transacciones)
        self.fra_transacciones.setStyleSheet("background-color: rgb(53, 28, 103);")
        self.fra_transacciones.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_transacciones.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_transacciones.setObjectName("fra_transacciones")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fra_transacciones)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tbl_transacciones = QtWidgets.QTableWidget(self.fra_transacciones)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tbl_transacciones.sizePolicy().hasHeightForWidth()
        )
        self.tbl_transacciones.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.tbl_transacciones.setFont(font)
        self.tbl_transacciones.setStyleSheet(
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
        self.tbl_transacciones.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.tbl_transacciones.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tbl_transacciones.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.SingleSelection
        )
        self.tbl_transacciones.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.tbl_transacciones.setObjectName("tbl_transacciones")
        self.tbl_transacciones.setColumnCount(0)
        self.tbl_transacciones.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tbl_transacciones)
        self.verticalLayout.addWidget(self.fra_transacciones)
        self.fra_inferior = QtWidgets.QFrame(frm_transacciones)
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

        self.retranslateUi(frm_transacciones)
        QtCore.QMetaObject.connectSlotsByName(frm_transacciones)

    def retranslateUi(self, frm_transacciones):
        _translate = QtCore.QCoreApplication.translate
        frm_transacciones.setWindowTitle(
            _translate("frm_transacciones", "Transacciones")
        )
        self.btn_cerrar.setText(_translate("frm_transacciones", "Cerrar"))


class VentanaTransacciones(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_frm_transacciones()
        self.ui.setupUi(self)
        self.ui.tbl_transacciones.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Stretch
        )
        self.ui.tbl_transacciones.verticalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Fixed
        )
        self.show()
