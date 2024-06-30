from PyQt6 import QtCore, QtGui, QtWidgets
from vista.libros import VentanaLibros
from vista.portada import VentanaPortada
from vista.facturas import VentanaFacturas
from vista.usuarios import VentanaUsuarios


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        MainWindow.setStyleSheet(
            "color: rgb(255,255,255);\n" "background-color: rgb(77, 44, 128);"
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fra_barra_superior = QtWidgets.QFrame(self.centralwidget)
        self.fra_barra_superior.setMaximumSize(QtCore.QSize(16777215, 20))
        self.fra_barra_superior.setStyleSheet("")
        self.fra_barra_superior.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_barra_superior.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fra_barra_superior.setObjectName("fra_barra_superior")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.fra_barra_superior)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fra_barra_titulo = QtWidgets.QFrame(self.fra_barra_superior)
        self.fra_barra_titulo.setStyleSheet("background-color: rgb(36, 16, 85);")
        self.fra_barra_titulo.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_barra_titulo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fra_barra_titulo.setObjectName("fra_barra_titulo")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.fra_barra_titulo)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lbl_titulo = QtWidgets.QLabel(self.fra_barra_titulo)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_titulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.horizontalLayout_5.addWidget(self.lbl_titulo)
        self.horizontalLayout_3.addWidget(self.fra_barra_titulo)
        self.fra_cerrar = QtWidgets.QFrame(self.fra_barra_superior)
        self.fra_cerrar.setMaximumSize(QtCore.QSize(20, 16777215))
        self.fra_cerrar.setStyleSheet("background-color: rgb(36, 16, 85);")
        self.fra_cerrar.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_cerrar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fra_cerrar.setObjectName("fra_cerrar")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.fra_cerrar)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_cerrar = QtWidgets.QPushButton(self.fra_cerrar)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cerrar.sizePolicy().hasHeightForWidth())
        self.btn_cerrar.setSizePolicy(sizePolicy)
        self.btn_cerrar.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(36, 16, 85);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(103, 64, 153);\n"
            "}"
        )
        self.btn_cerrar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("./resources/x.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.btn_cerrar.setIcon(icon)
        self.btn_cerrar.setIconSize(QtCore.QSize(18, 18))
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.horizontalLayout_4.addWidget(self.btn_cerrar)
        self.horizontalLayout_3.addWidget(self.fra_cerrar)
        self.verticalLayout.addWidget(self.fra_barra_superior)
        self.fra_contenido = QtWidgets.QFrame(self.centralwidget)
        self.fra_contenido.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_contenido.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fra_contenido.setObjectName("fra_contenido")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fra_contenido)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fra_barra_lateral = QtWidgets.QFrame(self.fra_contenido)
        self.fra_barra_lateral.setMinimumSize(QtCore.QSize(70, 0))
        self.fra_barra_lateral.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_barra_lateral.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fra_barra_lateral.setObjectName("fra_barra_lateral")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fra_barra_lateral)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fra_toggle = QtWidgets.QFrame(self.fra_barra_lateral)
        self.fra_toggle.setMaximumSize(QtCore.QSize(16777215, 70))
        self.fra_toggle.setStyleSheet("background-color: rgb(53, 28, 103);")
        self.fra_toggle.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_toggle.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fra_toggle.setObjectName("fra_toggle")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fra_toggle)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_toggle = QtWidgets.QPushButton(self.fra_toggle)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy)
        self.btn_toggle.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(53, 28, 103);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(103, 64, 153);\n"
            "}"
        )
        self.btn_toggle.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("./resources/menu1.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.btn_toggle.setIcon(icon1)
        self.btn_toggle.setIconSize(QtCore.QSize(34, 34))
        self.btn_toggle.setObjectName("btn_toggle")
        self.horizontalLayout_2.addWidget(self.btn_toggle)
        self.verticalLayout_2.addWidget(self.fra_toggle)
        self.fra_menu = QtWidgets.QFrame(self.fra_barra_lateral)
        self.fra_menu.setStyleSheet("background-color: rgb(53, 28, 103);")
        self.fra_menu.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_menu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fra_menu.setObjectName("fra_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fra_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.fra_opciones = QtWidgets.QFrame(self.fra_menu)
        self.fra_opciones.setStyleSheet("background-color: rgb(53, 28, 103);")
        self.fra_opciones.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fra_opciones.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fra_opciones.setObjectName("fra_opciones")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.fra_opciones)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_home = QtWidgets.QPushButton(self.fra_opciones)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.btn_home.setFont(font)
        self.btn_home.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255,255,255);\n"
            "    background-color: rgb(53, 28, 103);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(103, 64, 153);\n"
            "}"
        )
        self.btn_home.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap("./resources/home.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.btn_home.setIcon(icon2)
        self.btn_home.setIconSize(QtCore.QSize(30, 30))
        self.btn_home.setObjectName("btn_home")
        self.verticalLayout_4.addWidget(self.btn_home)
        self.btn_libros = QtWidgets.QPushButton(self.fra_opciones)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_libros.sizePolicy().hasHeightForWidth())
        self.btn_libros.setSizePolicy(sizePolicy)
        self.btn_libros.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.btn_libros.setFont(font)
        self.btn_libros.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255,255,255);\n"
            "    background-color: rgb(53, 28, 103);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(103, 64, 153);\n"
            "}"
        )
        self.btn_libros.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap("./resources/book.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.btn_libros.setIcon(icon3)
        self.btn_libros.setIconSize(QtCore.QSize(30, 30))
        self.btn_libros.setObjectName("btn_libros")
        self.verticalLayout_4.addWidget(self.btn_libros)
        self.btn_clientes = QtWidgets.QPushButton(self.fra_opciones)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clientes.sizePolicy().hasHeightForWidth())
        self.btn_clientes.setSizePolicy(sizePolicy)
        self.btn_clientes.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.btn_clientes.setFont(font)
        self.btn_clientes.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255,255,255);\n"
            "    background-color: rgb(53, 28, 103);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(103, 64, 153);\n"
            "}"
        )
        self.btn_clientes.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap("./resources/user.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.btn_clientes.setIcon(icon4)
        self.btn_clientes.setIconSize(QtCore.QSize(30, 30))
        self.btn_clientes.setObjectName("btn_clientes")
        self.verticalLayout_4.addWidget(self.btn_clientes)
        self.btn_proveedores = QtWidgets.QPushButton(self.fra_opciones)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_proveedores.sizePolicy().hasHeightForWidth()
        )
        self.btn_proveedores.setSizePolicy(sizePolicy)
        self.btn_proveedores.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.btn_proveedores.setFont(font)
        self.btn_proveedores.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255,255,255);\n"
            "    background-color: rgb(53, 28, 103);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(103, 64, 153);\n"
            "}"
        )
        self.btn_proveedores.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap("./resources/truck.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.btn_proveedores.setIcon(icon5)
        self.btn_proveedores.setIconSize(QtCore.QSize(30, 30))
        self.btn_proveedores.setObjectName("btn_proveedores")
        self.verticalLayout_4.addWidget(self.btn_proveedores)
        self.btn_facturas = QtWidgets.QPushButton(self.fra_opciones)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_facturas.sizePolicy().hasHeightForWidth())
        self.btn_facturas.setSizePolicy(sizePolicy)
        self.btn_facturas.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.btn_facturas.setFont(font)
        self.btn_facturas.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255,255,255);\n"
            "    background-color: rgb(53, 28, 103);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(103, 64, 153);\n"
            "}"
        )
        self.btn_facturas.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap("./resources/file-text.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.btn_facturas.setIcon(icon6)
        self.btn_facturas.setIconSize(QtCore.QSize(30, 30))
        self.btn_facturas.setObjectName("btn_facturas")
        self.verticalLayout_4.addWidget(self.btn_facturas)
        self.btn_costoso = QtWidgets.QPushButton(self.fra_opciones)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_costoso.sizePolicy().hasHeightForWidth())
        self.btn_costoso.setSizePolicy(sizePolicy)
        self.btn_costoso.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.btn_costoso.setFont(font)
        self.btn_costoso.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255,255,255);\n"
            "    background-color: rgb(53, 28, 103);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(103, 64, 153);\n"
            "}"
        )
        self.btn_costoso.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(
            QtGui.QPixmap("./resources/dollar-sign1.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.btn_costoso.setIcon(icon7)
        self.btn_costoso.setIconSize(QtCore.QSize(30, 30))
        self.btn_costoso.setObjectName("btn_costoso")
        self.verticalLayout_4.addWidget(self.btn_costoso)
        self.btn_economico = QtWidgets.QPushButton(self.fra_opciones)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_economico.sizePolicy().hasHeightForWidth()
        )
        self.btn_economico.setSizePolicy(sizePolicy)
        self.btn_economico.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.btn_economico.setFont(font)
        self.btn_economico.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255,255,255);\n"
            "    background-color: rgb(53, 28, 103);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(103, 64, 153);\n"
            "}"
        )
        self.btn_economico.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(
            QtGui.QPixmap("./resources/dollar-sign2.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.btn_economico.setIcon(icon8)
        self.btn_economico.setIconSize(QtCore.QSize(30, 30))
        self.btn_economico.setObjectName("btn_economico")
        self.verticalLayout_4.addWidget(self.btn_economico)
        self.btn_vendido = QtWidgets.QPushButton(self.fra_opciones)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_vendido.sizePolicy().hasHeightForWidth())
        self.btn_vendido.setSizePolicy(sizePolicy)
        self.btn_vendido.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.btn_vendido.setFont(font)
        self.btn_vendido.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255,255,255);\n"
            "    background-color: rgb(53, 28, 103);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(103, 64, 153);\n"
            "}"
        )
        self.btn_vendido.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(
            QtGui.QPixmap("./resources/star.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.btn_vendido.setIcon(icon9)
        self.btn_vendido.setIconSize(QtCore.QSize(30, 30))
        self.btn_vendido.setObjectName("btn_vendido")
        self.verticalLayout_4.addWidget(self.btn_vendido)
        self.verticalLayout_3.addWidget(
            self.fra_opciones, 0, QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.verticalLayout_2.addWidget(self.fra_menu)
        self.horizontalLayout.addWidget(self.fra_barra_lateral)
        self.frm_paginas = QtWidgets.QFrame(self.fra_contenido)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frm_paginas.sizePolicy().hasHeightForWidth())
        self.frm_paginas.setSizePolicy(sizePolicy)
        self.frm_paginas.setStyleSheet("background-color: rgb(77, 44, 128);")
        self.frm_paginas.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frm_paginas.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frm_paginas.setObjectName("frm_paginas")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frm_paginas)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stk_paginas = QtWidgets.QStackedWidget(self.frm_paginas)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stk_paginas.sizePolicy().hasHeightForWidth())
        self.stk_paginas.setSizePolicy(sizePolicy)
        self.stk_paginas.setObjectName("stk_paginas")
        self.verticalLayout_5.addWidget(self.stk_paginas)
        self.horizontalLayout.addWidget(self.frm_paginas)
        self.verticalLayout.addWidget(self.fra_contenido)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stk_paginas.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema gestión librería"))
        self.lbl_titulo.setText(_translate("MainWindow", "SISTEMA GESTIÓN LIBRERÍA"))


class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.pagina_home = VentanaPortada()
        self.pagina_libros = VentanaLibros()
        self.pagina_proveedores = VentanaUsuarios("Proveedores")
        self.pagina_clientes = VentanaUsuarios("Clientes")
        self.pagina_facturas = VentanaFacturas()
        self.ui.setupUi(self)
        self.ui.stk_paginas.addWidget(self.pagina_home)
        self.ui.stk_paginas.addWidget(self.pagina_libros)
        self.ui.stk_paginas.addWidget(self.pagina_clientes)
        self.ui.stk_paginas.addWidget(self.pagina_proveedores)
        self.ui.stk_paginas.addWidget(self.pagina_facturas)
        self.setWindowFlags(
            QtCore.Qt.WindowType.Window | QtCore.Qt.WindowType.CustomizeWindowHint
        )
        self.show()
