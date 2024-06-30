from PyQt6.QtGui import QRegularExpressionValidator, QPixmap
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtWidgets import QStyledItemDelegate, QLabel


class Validador:
    letras = QRegularExpressionValidator(QRegularExpression("^[\p{L}]+(\s[\p{L}]+)+?$"))
    letras_enteros = QRegularExpressionValidator(
        QRegularExpression("^[\p{L}0-9:.-]+(\s[\p{L}0-9:.-]+)+?$")
    )
    decimales = QRegularExpressionValidator(QRegularExpression("^[0-9]\d*(\.\d+)?$"))
    enteros = QRegularExpressionValidator(QRegularExpression("^[0-9]+$"))
    correo = QRegularExpressionValidator(QRegularExpression("^[a-zA-Z0-9_.@-]*$"))


class ReadOnlyDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        return


class ImageWidget(QLabel):
    def __init__(self, parent, image_path):
        QLabel.__init__(self, parent)
        self.setPixmap(QPixmap(image_path))
        self.setScaledContents(True)


def cedula_valida(cedula):
    return (
        sum(
            [
                int(cedula[i])
                if i % 2 != 0
                else int(cedula[i]) * 2
                if int(cedula[i]) * 2 < 9
                else int(cedula[i]) * 2 - 9
                for i in range(len(cedula))
            ]
        )
        % 10
        == 0
        and len(cedula) == 10
    )
