import pickle
from modelo.factura import Factura


class GestorFactura:
    numero = 0
    facturas: list[Factura] = []

    @staticmethod
    def agregar(factura):
        GestorFactura.facturas.append(factura)

    @staticmethod
    def eliminar(index):
        GestorFactura.facturas.pop(index)

    @staticmethod
    def index(numero):
        for i, factura in enumerate(GestorFactura.facturas):
            if factura.numero == numero:
                return i
        raise ValueError(f"No se ha encontrado una factura con número {numero}.")

    @staticmethod
    def sig_val():
        GestorFactura.numero += 1
        return GestorFactura.numero

    @staticmethod
    def grabar_datos():
        with open("./modelo/facturas.dat", "wb") as out_file1:
            pickle.dump(GestorFactura.facturas, out_file1)
            out_file1.flush()
            out_file1.close()
        with open("./modelo/n_f.dat", "wb") as out_file2:
            pickle.dump(GestorFactura.numero, out_file2)
            out_file2.flush()
            out_file2.close()

    @staticmethod
    def cargar_datos():
        with open("./modelo/facturas.dat", "rb") as in_file1:
            GestorFactura.facturas = pickle.load(in_file1)
            in_file1.close()
        with open("./modelo/n_f.dat", "rb") as in_file2:
            GestorFactura.numero = pickle.load(in_file2)
            in_file2.close()
